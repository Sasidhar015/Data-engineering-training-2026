cat > factory_quality_dag.py <<'EOF'
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import csv


def load_batches():
    with open("/opt/airflow/dags/factory_batches.csv", newline="") as file:
        rows = list(csv.DictReader(file))
    print("Batches loaded:", len(rows))
    return rows


def check_quality(ti):
    rows = ti.xcom_pull(task_ids="load_batches")
    review_ids = []
    for row in rows:
        units = int(row["units_produced"])
        defects = int(row["defective_units"])
        if defects > 0.05 * units:
            review_ids.append(row["batch_id"])
    print("Batches needing review:", review_ids)
    return {"total_batches": len(rows), "review_batches": review_ids}


def calculate_value(ti):
    rows = ti.xcom_pull(task_ids="load_batches")
    total_value = 0
    for row in rows:
        total_value += int(row["units_produced"]) * int(row["value_per_unit"])
    print("Total production value:", total_value)
    return total_value


def generate_report(ti):
    quality = ti.xcom_pull(task_ids="check_quality")
    total_value = ti.xcom_pull(task_ids="calculate_value")
    print("===== MANUFACTURING BATCH QUALITY REPORT =====")
    print("Total batches:", quality["total_batches"])
    print("Batches requiring review:", ", ".join(quality["review_batches"]))
    print("Total production value:", total_value)


with DAG(
    dag_id="factory_quality_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    load_task = PythonOperator(
        task_id="load_batches",
        python_callable=load_batches,
    )

    quality_task = PythonOperator(
        task_id="check_quality",
        python_callable=check_quality,
    )

    value_task = PythonOperator(
        task_id="calculate_value",
        python_callable=calculate_value,
    )

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    load_task >> [quality_task, value_task] >> report_task
EOF
