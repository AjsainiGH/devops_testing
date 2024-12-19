FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN  pip install -r requirements.txt

COPY testing.py .

ENTRYPOINT ["python3","testing.py"]

