FROM python:3.8-slim

WORKDIR /app

COPY /app/ .

EXPOSE 8080

RUN pip install -r requirements.txt

ENV NAME gzip-compression

CMD ["python", "gzip_compression.py"]
