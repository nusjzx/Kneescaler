FROM python:3.8-slim

RUN mkdir /app

WORKDIR /app

COPY . /app/

EXPOSE 8080

RUN pip install -r rnn_requirements.txt

ENV NAME rnn

CMD ["python", "rnn.py"]
