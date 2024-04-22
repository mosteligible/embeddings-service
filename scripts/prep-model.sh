#!/bin/sh

echo "Getting model from: https://huggingface.co/${HF_MODEL}"
git lfs install
git clone "https://huggingface.co/${HF_MODEL}" /srv

exec "$@"
