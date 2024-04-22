#!/bin/sh

git lfs install
git clone https://huggingface.co/${HF_MODEL}

exec "$@"
