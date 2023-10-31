FROM python:3.8-slim

WORKDIR /mnt/ustorage/ce7490_P1

COPY . /mnt/ustorage/ce7490_P1

EXPOSE 8080

RUN pip install -r requirements.txt

ENV NAME matmul

CMD ["python", "matmul.py"]
