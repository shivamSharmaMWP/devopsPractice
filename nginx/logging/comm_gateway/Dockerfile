FROM python:3.7-slim

RUN pip3 install --upgrade pip setuptools wheel

# install dependencies
ADD requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /opt/workdir

# for installing curl, handy for testing
RUN apt-get update && apt-get install -y curl && apt-get clean

CMD ["bash", "entry.sh"]
