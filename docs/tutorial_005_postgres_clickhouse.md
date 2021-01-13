#### Create ClickHouse database 

`docker run -it --rm --network src_airflow --link clh:clh-server yandex/clickhouse-client --host clh-server`


#### create database tutorial

`create database tutorial;`

#### Create Table

```
CREATE TABLE tutorial.pageview_counts (
    pagename String ,
    pageviewcount Int16 ,
    `index` Int16 ,
    datetime DateTime
)
ENGINE = MergeTree()
ORDER BY datetime

```

sample output

```
docker run -it --rm --network src_airflow --link clh:clh-server yandex/clickhouse-client --host clh-server
ClickHouse client version 20.12.4.5 (official build).
Connecting to clh-server:9000 as user default.
Connected to ClickHouse server version 20.12.4 revision 54442.

1ce68f37519c :) create database tutorial

CREATE DATABASE tutorial

Query id: 85ea68a7-b0f3-4292-8918-7c54fe60d58e

Ok.

0 rows in set. Elapsed: 0.009 sec.

1ce68f37519c :) CREATE TABLE tutorial.pageview_counts (
:-]     pagename String ,
:-]     pageviewcount Int16 ,
:-]     `index` Int16 ,
:-]     datetime DateTime
:-] )
:-] ENGINE = MergeTree()
:-] ORDER BY datetime

CREATE TABLE tutorial.pageview_counts
(
    `pagename` String,
    `pageviewcount` Int16,
    `index` Int16,
    `datetime` DateTime
)
ENGINE = MergeTree()
ORDER BY datetime

Query id: 088cbd67-361e-41d1-96aa-2284a1d06604

Ok.

0 rows in set. Elapsed: 0.007 sec.

1ce68f37519c :)
```

##### Trigger Dag
http://localhost:8080/admin/airflow/graph?dag_id=demo_200_postgres_clickhouse


See output as example

```

1ce68f37519c :) select * from tutorial.pageview_counts;

SELECT *
FROM tutorial.pageview_counts

Query id: eac6e04b-d30e-4451-8dc2-78742fa467ea

┌─pagename──┬─pageviewcount─┬─index─┬────────────datetime─┐
│ Apple     │            43 │     0 │ 2021-01-10 00:00:00 │
│ Google    │           552 │     1 │ 2021-01-10 00:00:00 │
│ Amazon    │            13 │     2 │ 2021-01-10 00:00:00 │
│ Microsoft │           242 │     3 │ 2021-01-10 00:00:00 │
│ Facebook  │           342 │     4 │ 2021-01-10 00:00:00 │
│ Amazon    │            21 │     5 │ 2021-01-10 01:00:00 │
│ Apple     │            53 │     6 │ 2021-01-10 01:00:00 │
│ Facebook  │           261 │     7 │ 2021-01-10 01:00:00 │
│ Microsoft │           246 │     8 │ 2021-01-10 01:00:00 │
│ Google    │           467 │     9 │ 2021-01-10 01:00:00 │
│ Microsoft │           212 │    10 │ 2021-01-10 02:00:00 │
│ Facebook  │           310 │    11 │ 2021-01-10 02:00:00 │
│ Apple     │            33 │    12 │ 2021-01-10 02:00:00 │
│ Google    │           486 │    13 │ 2021-01-10 02:00:00 │
│ Amazon    │            20 │    14 │ 2021-01-10 02:00:00 │
└───────────┴───────────────┴───────┴─────────────────────┘
```

