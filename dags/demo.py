import pendulum
import requests
from pathlib import Path

from airflow.decorators import dag, task

@dag(
    schedule="@daily",
    start_date=pendulum.datetime(2023, 12, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def demo_dag():
    """
    a simple demo dag
    """
    pass

demo_dag()
