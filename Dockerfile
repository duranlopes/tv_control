FROM python:3-slim

LABEL maintainer='Duran Lopes'

ADD . /app

WORKDIR /app

ENV PYTHONUNBUFEFERED 1

RUN pip install pip --upgrade && pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]