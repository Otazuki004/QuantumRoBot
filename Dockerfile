FROM python

WORKDIR /root/

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U -r requirements.txt

RUN apt install libjpeg-turbo

RUN python3 -m root
