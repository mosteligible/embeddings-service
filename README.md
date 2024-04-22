# General purpose embeddings generator

Build a fastapi server that allows you to use generate embeddings from any models in huggingface library, provided your machine is sufficient for it.

## Utilities required to run server

- Docker
- Make (optional): Optional because commands in Makefile can be executed separately in cli/terminal to get desired result if adding `make` is not desirable.

## Build image

Run `make docker-image` command and it will create a docker image with name `embedding-srv:0.1.0`.

## Run docker image

To run image, following environment variables are required:
- LLM_MODEL_NAME
- HF_MODEL

LLM_MODEL_NAME is the name of model in hugging-face library to be used for embedding.

HF_MODEL refers to path and model name associated with the model in hugging face library.

For example,  [GritLM/GritLM-7B](https://huggingface.co/GritLM/GritLM-7B) model can be used with following environment variables:
```
LLM_MODEL_NAME=GritLM-7B
HF_MODEL=GritLM/GritLM-7B
```

Add the above variables in a .env file at the root level of this project.

Then run command: `make docker-run`.
