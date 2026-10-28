from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def ingest():   print("ingest")
def validate(): print("validate")
def train():    print("train")
def evaluate(): print("evaluate")
def deploy():   print("deploy")

with DAG("ml_training_pipeline", start_date=datetime(2026, 1, 1),
         schedule="@weekly", catchup=False) as dag:
    t1 = PythonOperator(task_id="ingest",   python_callable=ingest)
    t2 = PythonOperator(task_id="validate", python_callable=validate)
    t3 = PythonOperator(task_id="train",    python_callable=train)
    t4 = PythonOperator(task_id="evaluate", python_callable=evaluate)
    t5 = PythonOperator(task_id="deploy",   python_callable=deploy)
    t1 >> t2 >> t3 >> t4 >> t5
