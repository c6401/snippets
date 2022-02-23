FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update &&\
    apt-get install -y --no-install-recommends {{ packages }}

RUN locale-gen en_US.UTF-8

ENV LANG='en_US.UTF-8'
ENV LC_ALL='en_US.UTF-8'
ENV LANGUAGE='en_US.UTF-8'

RUN useradd -ms /bin/bash app
USER app
