#### Check database schema

When building database, we already initialized database.
See db/Dockerfile.

The database will be used as Airflow Postgres Connection in docker-compose.yml

```
AIRFLOW_CONN_MY_POSTGRES_CONN: 'postgresql://airflow:airflow@postgres:5432/airflow'
```


Trigger Dag

http://localhost:8080/admin/airflow/tree?dag_id=demo_100_postgres_operator&num_runs=&root=


##### Check data inserted 

```
airflow-# select * from pageview_counts ;
 pagename  | pageviewcount |      datetime
-----------+---------------+---------------------
 Apple     |            43 | 2021-01-10 00:00:00
 Google    |           552 | 2021-01-10 00:00:00
 Amazon    |            13 | 2021-01-10 00:00:00
 Microsoft |           242 | 2021-01-10 00:00:00
 Facebook  |           342 | 2021-01-10 00:00:00
 Amazon    |            21 | 2021-01-10 01:00:00
 Apple     |            53 | 2021-01-10 01:00:00
 Facebook  |           261 | 2021-01-10 01:00:00
 Microsoft |           246 | 2021-01-10 01:00:00
 Google    |           467 | 2021-01-10 01:00:00
 ```

