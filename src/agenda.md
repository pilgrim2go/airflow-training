# connect clh
docker run -it --rm --network chapter4_airflow --link chapter4_clh_1:clickhouse-server yandex/clickhouse-client --host clickhouse-server

# create clh database/table


# install python
pip install marshmallow==2.21.0
pip install pandahouse
pip install pyathena


# issues

ERROR - The conn_id `my_postgres` isn't defined

create connection http://localhost:8080/admin/connection/edit/?id=13&url=%2Fadmin%2Fconnection%2F


Adhoc query

http://localhost:8080/admin/queryview/

---

[2020-12-11 07:02:05,708] {taskinstance.py:1150} ERROR - The conn_id `clickhouse_test` isn't defined


[2020-12-11 07:08:30,218] {clickhouse_hook.py:81} INFO - 
                SELECT *
                FROM tutorial.visits_v1
            
[2020-12-11 07:08:30,224] {taskinstance.py:1150} ERROR - Code: 81.
DB::Exception: Database `tutorial` doesn't exist. Stack trace:


create database tutorial;
CREATE TABLE tutorial.pageview_counts (
    pagename String ,
    pageviewcount Int16 ,
    `index` Int16 ,

    datetime DateTime
)
ENGINE = MergeTree()
ORDER BY datetime


```
pandahouse.http.ClickhouseException: b'Code: 27, e.displayText() = DB::Exception: Cannot parse input: expected \'"\' before: \'.000000"\\n1,"Facebook",358,"2020-12-08 01:00:00.000000"\\n2,"Apple",60,"2020-12-08 01:00:00.000000"\\n3,"Google",536,"2020-12-08 01:00:00.000000"\\n4,"Microsoft",300,"\': (at row 1)\n\nRow 1:\nColumn 0,   name: index,         type: Int16,    parsed text: "0"\nColumn 1,   name: pagename,      type: String,   parsed text: "<DOUBLE QUOTE>Amazon<DOUBLE QUOTE>"\nColumn 2,   name: pageviewcount, type: Int16,    parsed text: "17"\nColumn 3,   name: datetime,      type: DateTime, parsed text: "<DOUBLE QUOTE>2020-12-08 01:00:00"ERROR: DateTime must be in YYYY-MM-DD hh:mm:ss or NNNNNNNNNN (unix timestamp, exactly 10 digits) format.\nCode: 27, e.displayText() = DB::Exception: Cannot parse input: expected \'"\' before: \'.000000"\\n1,"Facebook",358,"2020-12-08 01:00:00.000000"\\n2,"Apple",60,"2020-12-08 01:00:00.000000"\\n3,"Google",536,"2020-12-08 01:00:00.000000"\\n4,"Microsoft",300,"\' (version 20.12.3.3 (official build))\n\n (version 20.12.3.3 (official build))\n'
[2020-12-11 07:15:10,754] {taskinstance.py:1194} INFO - Marking task as FAILED. dag_id=demo_300_postgres_2_clickhouse, task_id=load, execution_date=20201211T071431, start_date=20201211T071510, end_date=20201211T071510
[2020-12-11 07:15:15,635] {local_task_job.py:102} INFO - Task exited with return code 1
```