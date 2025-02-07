from contextlib import contextmanager, redirect_stderr, redirect_stdout
import llm
from llama_cpp import Llama
import llama_cpp._logger as llama_logger
import importlib.resources
import logging
import os

llama_logger.logger.setLevel(logging.CRITICAL)

gguf_path = str(
    importlib.resources.files("llm_smollm2").joinpath("SmolLM2-135M-Instruct.Q4_1.gguf")
)


@llm.hookimpl
def register_models(register):
    register(SmolLM2("SmolLM2", gguf_path))


class SmolLM2(llm.Model):
    can_stream = True

    def __init__(
        self,
        model_id,
        model_path,
    ):
        self.model_id = model_id
        self.model_path = model_path
        self._model = None

    def get_model(self):
        if self._model is None:
            with suppress_output():
                self._model = Llama(model_path=self.model_path, verbose=False)
        return self._model

    def execute(self, prompt, stream, response, conversation):
        messages = []
        current_system = None
        if conversation is not None:
            for prev_response in conversation.responses:
                if (
                    prev_response.prompt.system
                    and prev_response.prompt.system != current_system
                ):
                    messages.append(
                        {"role": "system", "content": prev_response.prompt.system}
                    )
                    current_system = prev_response.prompt.system
                messages.append(
                    {"role": "user", "content": prev_response.prompt.prompt}
                )
                messages.append({"role": "assistant", "content": prev_response.text()})
        if prompt.system and prompt.system != current_system:
            messages.append({"role": "system", "content": prompt.system})
        messages.append({"role": "user", "content": prompt.prompt})

        model = self.get_model()

        if not stream:
            completion = model.create_chat_completion(messages=messages)
            yield completion["choices"][0]["message"]["content"]
        else:
            completion = model.create_chat_completion(messages=messages, stream=True)
            for chunk in completion:
                choice = chunk["choices"][0]
                delta_content = choice.get("delta", {}).get("content")
                if delta_content is not None:
                    yield delta_content


@contextmanager
def suppress_output():
    """
    Suppresses all stdout and stderr output within the context.
    """
    with open(os.devnull, "w") as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            yield
