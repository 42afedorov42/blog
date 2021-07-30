# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/blog

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["sh", "/usr/src/blog/entrypoint.sh"]