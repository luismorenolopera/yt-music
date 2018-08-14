from ubuntu:16.04
MAINTAINER Luis Moreno "l.david1929@gmail.com"

RUN mkdir /code
WORKDIR /code
COPY . ./

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:jonathonf/python-3.6 && \
    apt-get install -y vim && \
    apt-get install -y git && \
    apt-get install -y ffmpeg && \
    apt-get update && \
    apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
    python3.6 -m pip install pip --upgrade

RUN pip install -r requirements.txt
RUN python3.6 ./ytmusic/manage.py makemigrations && python3.6 ./ytmusic/manage.py migrate
VOLUME /data
CMD python3.6 ./ytmusic/manage.py runserver 0.0.0.0:8000
EXPOSE 8000
