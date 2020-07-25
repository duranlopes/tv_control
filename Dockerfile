FROM python:3-slim

LABEL maintainer='Duran Lopes'

ADD . /app

WORKDIR /app

ENV PYTHONUNBUFEFERED 1 
ENV TV_IP 192.168.25.102
ENV TV_MAC_ADDRESS BC:8C:CD:30:8B:9B

RUN pip install pip --upgrade && pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]