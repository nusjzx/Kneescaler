FROM python:3.8-slim

WORKDIR /app

COPY . /app/ .

EXPOSE 8080

RUN pip install -r matmul_requirements.txt

ENV NAME matmul

CMD ["python", "matmul.py"]
