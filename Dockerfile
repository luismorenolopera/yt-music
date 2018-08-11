FROM ubuntu:16.04
MAINTAINER Luis Moreno "l.david1929@gmail.com"

RUN mkdir /ytmusic
WORKDIR /ytmusic/ytmusic
ADD requirements.txt /ytmusic/

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git
RUN apt-get install -y ffmpeg

RUN python3.6 -m pip install pip --upgrade

RUN pip install -r requirements.txt
ADD . /ytmusic/
