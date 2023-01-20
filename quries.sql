/* Question 3. Count records - How many taxi trips were totally made on January 15? */
select count(1)
from green_taxi
where cast(lpep_pickup_datetime as varchar) like '____-01-15%'
and cast(lpep_dropoff_datetime as varchar) like '____-01-15%';

/* Question 4. Largest trip for each day - Which was the day with the largest trip distance Use the pick up time for your calculations. */
select lpep_pickup_datetime, trip_distance
from green_taxi
order by trip_distance desc;

/*Question 5: The number of passengers  (Multiple choice)
In 2019-01-01 how many trips had 2 and 3 passengers? */
select count(passenger_count) as total
from green_taxi
where cast(lpep_pickup_datetime as varchar) like '2019-01-01%'
and passenger_count = 2;

select count(passenger_count) as total
from green_taxi
where cast(lpep_pickup_datetime as varchar) like '2019-01-01%'
and passenger_count = 3;

/* Question 6: Largest tip (Multiple choice)
For the passengers picked up in the Astoria Zone which was the drop up zone that had the largest tip? */
select "LocationID", "Zone", tip_amount, "DOLocationID"
from zones
full outer join green_taxi 
on zones."LocationID" = green_taxi."PULocationID"
where "Zone" = 'Astoria'
order by tip_amount desc;


select "Zone"
from zones
where "LocationID" = 146;