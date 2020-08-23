FROM python:3.9.0rc1-buster

WORKDIR /usr/src/app

COPY FinnAI.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","./FinnAI.py"]