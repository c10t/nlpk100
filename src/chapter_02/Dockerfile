FROM python:3.7.0-alpine

COPY . /home/nlpk/
WORKDIR /home/nlpk/
RUN pwd
RUN ls -alh

CMD ["sh", "scripts/00_wordcount.sh"]
