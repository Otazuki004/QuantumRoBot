FROM python:3.10.0

WORKDIR /root/

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U -r requirements.txt

RUN pkg install libjpeg-turbo

CMD ["python3","-m","bot"]
