FROM python:3.7-slim

ADD requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
