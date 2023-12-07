import pendulum
import requests
from pathlib import Path

from airflow.decorators import dag, task

@task
def file_orders():
    """
    get raw_orders.csv and save to data/raw_orders
    """
    url = "https://raw.githubusercontent.com/dbt-labs/jaffle_shop/main/seeds/raw_orders.csv"
    data = requests.get(url)
    folder = Path("data/raw_orders")
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"raw_orders.csv"
    path.write_text(data.text)


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
    file_orders()


demo_dag()
