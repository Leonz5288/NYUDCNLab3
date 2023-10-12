FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install Flask requests

COPY . .

CMD [ "python", "./us.py" ]
