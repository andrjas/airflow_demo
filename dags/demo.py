import pendulum
import requests
from pathlib import Path

from airflow.decorators import dag, task

@task
def file_orders(ds=None):
    """
    get raw_orders.csv and save to data/raw_orders
    """
    url = "https://raw.githubusercontent.com/dbt-labs/jaffle_shop/main/seeds/raw_orders.csv"
    data = requests.get(url)
    folder = Path("data/raw_orders")
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"raw_orders_{ds}.csv"
    path.write_text(data.text)
    return path.as_posix()


@task
def orders(file_orders_path, ds=None):
    file_orders = Path(file_orders_path)
    num_lines = len(file_orders.read_text().splitlines())
    return num_lines

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

    orders(file_orders())

demo_dag()

# im terminal ausführen:
# airflow dags backfill demo_dag  --start-date 2023-11-28 --end-date 2023-11-30
