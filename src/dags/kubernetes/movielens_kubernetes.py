import os

from airflow import DAG, utils as airflow_utils
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume import Volume
from airflow.contrib.kubernetes.volume_mount import VolumeMount


# print(open('"/tmp/config"').read())

with DAG(
    dag_id="chapter11_movielens_kubernetes",
    description="Fetches ratings from the Movielens API using kubernetes.",
    start_date=airflow_utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:

    kubeconfig_volume_config = {
        # "secret": {
        #     "secretName": "local-dev-secrets-kubeconfig"
        # }
    }
    volume_mounts = [
        VolumeMount(
        "data-volume", mount_path="/data", sub_path=None, read_only=False
    ),
        # VolumeMount('local-dev-secrets-kubeconfig', mount_path='/root/.kube/config', sub_path=None, read_only=True),    
    ]

    volume_config = {"persistentVolumeClaim": {"claimName": "data-volume"}}
    
    volumes = [
        Volume(name="data-volume", configs=volume_config),
        
        Volume(name='local-dev-secrets-kubeconfig', configs=kubeconfig_volume_config),
    ]
    

    fetch_ratings = KubernetesPodOperator(
        task_id="fetch_ratings",
        image="airflowbook/movielens-fetch",
        cmds=["fetch-ratings"],
        arguments=[
            "--start_date",
            "2021-01-09",
            "--end_date",
            "{{next_ds}}",
            "--output_path",
            "/data/ratings/2021-01-09.json",
            "--user",
            os.environ["MOVIELENS_USER"],
            "--password",
            os.environ["MOVIELENS_PASSWORD"],
            "--host",
            os.environ["MOVIELENS_HOST"],
        ],
        namespace="airflow",
        name="fetch-ratings",
        cluster_context="docker-desktop",
        is_delete_operator_pod=False,
        volumes=volumes,
        volume_mounts=volume_mounts,
        in_cluster=False,
        config_file="/root/.kube/config",

    )

    rank_movies = KubernetesPodOperator(
        task_id="rank_movies",
        image="airflowbook/movielens-rank",
        cmds=["rank-movies"],
        arguments=[
            "--input_path",
            "/data/ratings/2021-01-09.json",
            "--output_path",
            "/data/rankings/2021-01-09.csv",
        ],
        namespace="airflow",
        name="rank-movies",
        cluster_context="docker-desktop",
        is_delete_operator_pod=False,
        
        volumes=volumes,
        volume_mounts=volume_mounts,
        in_cluster=False,
        config_file="/root/.kube/config",
        
    )

    fetch_ratings >> rank_movies
