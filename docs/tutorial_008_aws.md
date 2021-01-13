Create CloudFormation Resource

`make aws`

Waiting for CF to finish and update .env

`cp .env.example .env`

```
AWS_ACCESS_KEY=AKIAZUFR7J**********
AWS_ACCESS_SECRET=SeOtrx2RppvPnL3npC**********
RATINGS_BUCKET=training-airflow-ratings
RANKINGS_BUCKET=training-airflow-rankings
CRAWLER_NAME=ratings-crawler
```

Note: when docker-compose up, it will check *.env* and apply these environment as following file

```
  airflow:
    build: ../docker
    image: manning-airflow:latest
    networks:
      - airflow
    environment:
      AWS_DEFAULT_REGION: us-west-2
      AIRFLOW_CONN_MY_AWS_CONN: 's3://?aws_access_key_id=${AWS_ACCESS_KEY}&aws_secret_access_key=${AWS_ACCESS_SECRET}'
      AIRFLOW_CONN_MY_POSTGRES_CONN: 'postgresql://airflow:airflow@postgres:5432/airflow'
      RATINGS_BUCKET: ${RATINGS_BUCKET}
      RANKINGS_BUCKET: ${RANKINGS_BUCKET}
      CRAWLER_NAME: ${CRAWLER_NAME}
```


Run Dag http://localhost:8080/admin/airflow/tree?dag_id=demo_aws_usecase