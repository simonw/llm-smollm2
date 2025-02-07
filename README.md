# llm-smollm2

[![PyPI](https://img.shields.io/pypi/v/llm-smollm2.svg)](https://pypi.org/project/llm-smollm2/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-smollm2?include_prereleases&label=changelog)](https://github.com/simonw/llm-smollm2/releases)
[![Tests](https://github.com/simonw/llm-smollm2/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/llm-smollm2/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-smollm2/blob/main/LICENSE)

SmolLM2-135M-Instruct.Q4_1 for LLM

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-smollm2
```
## Usage

This plugin bundles a full copy of the [SmolLM2-135M-Instruct.Q4_1](https://huggingface.co/QuantFactory/SmolLM2-135M-Instruct-GGUF/blob/ab810cf68114990406fdf996510dd3d3c6adbdf5/SmolLM2-135M-Instruct.Q4_1.gguf) quantized version of the [SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) model by [HuggingFaceTB](https://huggingface.co/HuggingFaceTB).

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-smollm2
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
