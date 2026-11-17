cat > atm_cash_dag.py <<'EOF'
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import csv


def load_atms():
    with open('/opt/airflow/dags/atm_cash.csv', newline='') as file:
        records = list(csv.DictReader(file))
    print('ATM records loaded:', len(records))
    return records


def identify_low_cash(ti):
    records = ti.xcom_pull(task_ids="load_atms")
    low_cash_ids = []
    for row in records:
        cash = int(row["cash_available"])
        demand = int(row["daily_demand"])
        if cash < demand:
            low_cash_ids.append(row["atm_id"])
    print("Low-cash ATMs:", low_cash_ids)
    return {"atm_count": len(records), "low_cash_atms": low_cash_ids}


def calculate_total_cash(ti):
    records = ti.xcom_pull(task_ids="load_atms")
    total_cash = 0
    for row in records:
        total_cash += int(row["cash_available"])
    print("Total available cash:", total_cash)
    return total_cash


def generate_report(ti):
    low = ti.xcom_pull(task_ids="identify_low_cash")
    total_cash = ti.xcom_pull(task_ids="calculate_total_cash")
    print("===== ATM CASH REPLENISHMENT REPORT =====")
    print("Number of ATMs:", low["atm_count"])
    print("Low-cash ATMs:", ", ".join(low["low_cash_atms"]))
    print("Total available cash:", total_cash)


with DAG(
    dag_id="atm_cash_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,) as dag:

    load_task = PythonOperator(
        task_id="load_atms",
        python_callable=load_atms,)

    low_cash_task = PythonOperator(
        task_id="identify_low_cash",
        python_callable=identify_low_cash,)

    total_cash_task = PythonOperator(
        task_id="calculate_total_cash",
        python_callable=calculate_total_cash,)

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,)

    load_task >> [low_cash_task, total_cash_task] >> report_task
EOF
