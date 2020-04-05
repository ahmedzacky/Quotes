FROM python:3.6.9
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN apt install python3-dev -y
RUN apt install build-essential -y
RUN pip install --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
