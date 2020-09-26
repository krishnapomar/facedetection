FROM python:3.7-alpine

COPY src/ /app/src

COPY template/ /app

COPY requirements.txt /app

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python3", "/app/src/server.py"]