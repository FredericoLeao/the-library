FROM python:3

WORKDIR /home/thelibrary/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
