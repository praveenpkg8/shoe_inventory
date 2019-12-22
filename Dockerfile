from ubuntu:18.04

run apt-get update

run apt-get install -y python3 python3-pip

run apt-get install -y redis-server && \
    apt-get clean

copy . /app

workdir /app

run pip3 install -r requirements.txt


expose 5000

entrypoint ["python3"]
cmd ["app.py"]