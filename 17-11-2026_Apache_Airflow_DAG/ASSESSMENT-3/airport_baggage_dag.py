cat > airport_baggage_dag.py <<'EOF'
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import csv


def load_baggage():
    with open('/opt/airflow/dags/airport_baggage.csv', newline='') as file:
        records = list(csv.DictReader(file))
    print('Baggage records loaded:', len(records))
    return records


def identify_review_bags(ti):
    records = ti.xcom_pull(task_ids="load_baggage")
    review_ids = []
    for row in records:
        weight = int(row["weight_kg"])
        if row["screening_status"] == "Review" or weight > 23:
            review_ids.append(row["bag_id"])
    print("Bags requiring review:", review_ids)
    return {"bag_count": len(records), "review_bags": review_ids}


def calculate_total_weight(ti):
    records = ti.xcom_pull(task_ids="load_baggage")
    total_weight = 0
    for row in records:
        total_weight += int(row["weight_kg"])
    print("Total baggage weight:", total_weight)
    return total_weight
EOF



cat >> airport_baggage_dag.py <<'EOF'


def generate_report(ti):
    review = ti.xcom_pull(task_ids="identify_review_bags")
    total_weight = ti.xcom_pull(task_ids="calculate_total_weight")
    print("===== AIRPORT BAGGAGE SCREENING REPORT =====")
    print("Number of bags:", review["bag_count"])
    print("Bags requiring review:", ", ".join(review["review_bags"]))
    print("Total baggage weight (kg):", total_weight)


with DAG(
    dag_id="airport_baggage_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,) as dag:

    load_task = PythonOperator(
        task_id="load_baggage",
        python_callable=load_baggage,)

    review_task = PythonOperator(
        task_id="identify_review_bags",
        python_callable=identify_review_bags,)

    weight_task = PythonOperator(
        task_id="calculate_total_weight",
        python_callable=calculate_total_weight,)

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,)

    load_task >> [review_task, weight_task] >> report_task
EOF
