# from datetime import datetime

# from airflow import DAG
# from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

# DAG_ID = "example_databricks_operator"

# with DAG(
#     dag_id=DAG_ID,
#     schedule="@daily",
#     start_date=datetime(2021, 1, 1),
#     tags=["example"],
#     catchup=False,
# ) as dag:
#     new_cluster = {
#         "spark_version": "13.3.x-scala2.12",
#         "node_type_id": "Standard_F4",
#         "num_workers": 1,
#     }

#     load_data_params = {
#         "new_cluster": new_cluster,
#         # "existing_cluster_id": "1012-035013-qbn9vg7j",
#         "notebook_task": {
#             "notebook_path": "/Users/arjasanow@infomotion.de/load_data",
#         },
#     }

#     load_data = DatabricksSubmitRunOperator(task_id="load_data", json=load_data_params)

#     display_data_params = {
#         "new_cluster": new_cluster,
#         # "existing_cluster_id": "1012-035013-qbn9vg7j",
#         "notebook_task": {
#             "notebook_path": "/Users/arjasanow@infomotion.de/display_data",
#         },
#     }

#     display_data = DatabricksSubmitRunOperator(task_id="display_data", json=display_data_params)

#     load_data >> display_data

