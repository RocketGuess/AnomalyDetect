FROM ubuntu:16.04
MAINTAINER Vladislav Pika
RUN apt-get update && \
    apt-get -y install python3-pip python3-dev

ADD requirements.txt ./requirements.txt
ADD server ./server

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD ["python3", "-u", "server/server.py"]
