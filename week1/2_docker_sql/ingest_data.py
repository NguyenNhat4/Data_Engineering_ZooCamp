#!/usr/bin/env python
# coding: utf-8
import os
import argparse
import pandas as pd 
from sqlalchemy import create_engine # type: ignore
import argparse
from time import time

def main(params):
    username = params.username
    password = params.password 
    host = params.host
    port = params.port
    table_name = params.table_name 
    db = params.db
    url = params.url
    csv_name = 'output.csv'

    
    os.system(f"wget {url} -O {csv_name}")
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db}')

    

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df.head(n=0).to_sql(name=table_name , con=engine, if_exists='replace')
    df.to_sql(name=table_name , con=engine, if_exists='append')





    while True:
        t_start = time()
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name='yellow_taxi_data' , con=engine, if_exists='append')
        t_end = time()
        print('insert another chunk, took %.3f second' % (t_end-t_start))
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ingest csv data to')
    parser.add_argument('--username', help='username for postgres')
    parser.add_argument('--password', help='password for  postgres')
    parser.add_argument('--host', help='host for  postgres')
    parser.add_argument('--port', help='port for  postgres')
    parser.add_argument('--db', help='database name for  postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to ')
    parser.add_argument('--url', help='url of the csv')
    args = parser.parse_args()
    main(args)



