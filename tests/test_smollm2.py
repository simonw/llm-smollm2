import llm


def test_model():
    model = llm.get_model("SmolLM2")
    response = model.prompt("The capital of France is")
    assert "paris" in response.text().lower()
