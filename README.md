# de-zoomcamp

1. Setup Docker
2. Run docker container with Ubuntu, Python3, pandas images
3. Install (for macOS): brew install pgcliCancel changes
4. Create the Dockerfile
5. Create the script for loading dataset from URL 

Datasets: wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz

Dataset zones: wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv

6. Setup pgAdmin
7. Create the network in the Docker for run python and postgres containers
8. Dockerizing the ingestion script from jupyter

jupyter nbconvert --to=script ingest_taxi_data.ipynb

9. Run the python script 
10. Build container:

docker build -t taxi_container:v001 .

11. Create docker-compose.yaml
12. Run docker-compose and connect to pgAdmin manually
