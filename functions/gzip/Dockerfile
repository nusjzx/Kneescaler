FROM python:3.8-slim

RUN mkdir /app

WORKDIR /app

COPY . /app/

EXPOSE 8080

RUN pip install -r gzip_requirements.txt

ENV NAME gzip_compression

CMD ["python", "gzip_compression.py"]
