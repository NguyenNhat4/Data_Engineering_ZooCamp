FROM python:3.9

RUN apt-get update && apt-get install -y bash
RUN apt-get install wget
RUN 
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY ingest_data.py ingest_data.py


ENTRYPOINT [ "python","ingest_data.py" ] 