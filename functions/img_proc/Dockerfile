FROM python:3.8-slim

RUN mkdir /app

WORKDIR /app

COPY . /app/

EXPOSE 8080

RUN pip install -r img_proc_requirements.txt

ENV NAME img_proc

CMD ["python", "img_proc.py"]
