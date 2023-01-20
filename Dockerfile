#run base image
FROM python:3.11.1

#command when we run the image(create new image overstad)
RUN pip3 install pandas sqlalchemy psycopg2 requests

#create directory
WORKDIR /app
#add the file pipeline (1st argument - name of file, 2 - distination,main folder in our case)
COPY ingest_taxi_data.py ingest_taxi_data.py

ENTRYPOINT [ "python3", "ingest_taxi_data.py" ]