FROM ubuntu

RUN apt-get update && apt-get install -y python3

ADD test /test

CMD python3 /test/test.py
