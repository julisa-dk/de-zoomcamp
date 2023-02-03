#!/usr/bin/env python
# coding: utf-8

import argparse
import pandas as pd

from sqlalchemy import create_engine
from time import time

import requests 

from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
from prefect_sqlalchemy import SqlAlchemyConnector

@task(log_prints=True, retries=3, cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract_data(url):
    csv_name = url.split("/")[-1]
    with open(csv_name, "wb") as f:
        r = requests.get(url)
        f.write(r.content)
    
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=10000, on_bad_lines='skip')
    
    df = next(df_iter)
   
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    return df

@task(log_prints=True)
def transform_data(df):
    print(f"pre: missing passenger count: {df['passenger_count'].isin([0]).sum()}")
    df = df[df['passenger_count'] != 0]
    print(f"post: missing passenger count: {df['passenger_count'].isin([0]).sum()}")
    return df

# add task for manage data by Prefect
@task(log_prints=True, retries=3)
def ingest_data(table_name, df):
    connection_block = SqlAlchemyConnector.load("postgres-connector")     #connect by connector which created in orion

    with connection_block.get_connection(begin=False) as engine:

        df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

        df.to_sql(name=table_name, con=engine, if_exists='append')

@flow(name="Subflow", log_prints=True)
def log_subflow(table_name:str):
    print("Logging Subflow for: {table_name}")
    
# add flow for manage the main flow by Perfect
@flow(name="Ingest Flow")
def main_flow(table_name: str):                       #can add parameters as for function

    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-01.csv.gz"
    log_subflow(table_name)
    raw_data = extract_data(url)
    data = transform_data(raw_data)
    ingest_data(table_name, data)

if __name__ == '__main__':
    main_flow("green_taxi")              #run main flow 