FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN apt update

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "crud.py"]
