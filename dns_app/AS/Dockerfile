FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . .

CMD [ "python", "./as.py" ]
