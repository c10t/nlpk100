FROM python:3.7-alpine

ADD . /home/code
WORKDIR /home/code
RUN pip install -r requirements.txt

CMD ["python", "-m", "http.server", "8000"]
