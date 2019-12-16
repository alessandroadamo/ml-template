FROM python:3.6.9-buster

ARG UID
ENV UID=1000

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN adduser --uid $UID --disabled-password user
WORKDIR /home/user

RUN mkdir -p lib/models

#COPY lib/models/model-latest.joblib lib/models/
#COPY lib/models/model-latest.md5 lib/models/
#COPY lib/models/model-latest.sha1 lib/models/
VOLUME /home/user/lib/models/

COPY app app
COPY startup.sh startup.sh

RUN chown user -R lib/models
RUN chown user -R app
RUN chmod +x startup.sh
RUN chown user -R startup.sh

USER user

COPY config.ini config.ini
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

SHELL [ "/bin/bash", "-c" ]

ENV FLASK_APP /home/user/app/app.py

EXPOSE 5000
CMD [ "./startup.sh"  ]
