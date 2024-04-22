#!/bin/bash

num_processes=$(grep ^cpu\\scores /proc/cpuinfo | uniq |  awk '{print $4}')

gunicorn main:app \
    --workers "${num_processes}" \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000
