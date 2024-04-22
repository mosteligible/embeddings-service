FROM python:3.9.19-bullseye

COPY requirements.txt /tmp
COPY ./scripts/cmd.sh /tmp
COPY ./scripts/prep-model.sh /srv
COPY ./server /app

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt --no-cache-dir
RUN apt-get install -y \
    git \
    git-lfs

WORKDIR /app

ENTRYPOINT [ "/srv/prep-model.sh" ]

CMD [ "/tmp/cmd.sh" ]
