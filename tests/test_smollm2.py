import llm
import pytest


@pytest.mark.parametrize("no_stream", (False, True))
def test_model(no_stream):
    model = llm.get_model("SmolLM2")
    kwargs = {}
    if no_stream:
        kwargs["stream"] = False
    response = model.prompt("The capital of France is", **kwargs)
    assert "paris" in response.text().lower()
