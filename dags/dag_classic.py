# from datetime import datetime
# import requests
# from pathlib import Path

# from airflow import DAG
# from airflow.operators.python import PythonOperator


# def file_orders(ds=None, ti=None):
#     """
#     get raw_orders.csv and save to data/raw_orders
#     """
#     url = "https://raw.githubusercontent.com/dbt-labs/jaffle_shop/main/seeds/raw_orders.csv"
#     data = requests.get(url)
#     folder = Path("data/raw_orders")
#     folder.mkdir(parents=True, exist_ok=True)
#     path = folder / f"{ds}.csv"
#     path.write_text(data.text)
#     # return path.as_posix()
#     ti.xcom_push(key="file_orders_path", value=path.as_posix())


# def orders(ds=None, ti=None):
#     file_orders_path = ti.xcom_pull(key="file_orders_path", task_ids="file_orders")
#     file_orders = Path(file_orders_path)
#     num_lines = len(file_orders.read_text().splitlines())
#     # return num_lines
#     ti.xcom_push(key="num_lines", value=num_lines)



# with DAG(
#     dag_id="demo_dag_classic",
#     schedule="@daily",
#     start_date=datetime(2023, 12, 1),
#     tags=["example"],
#     catchup=False,
# ) as dag:
    
#     file_orders_task = PythonOperator(
#         task_id="file_orders",
#         python_callable=file_orders,
#     )

#     orders_task = PythonOperator(
#         task_id="orders",
#         python_callable=orders,
#     )

#     file_orders_task >> orders_task
