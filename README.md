# D608 Data Pipelines Project – Airflow + Redshift

This project is part of the WGU D608 course. It demonstrates a complete ETL pipeline built with Apache Airflow that extracts JSON data from AWS S3, stages it in Amazon Redshift, transforms it into a star schema, and performs automated data quality checks.

---

## 📁 Project Structure

```
dags/
  └── final_project.py
plugins/
  └── operators/
      ├── __init__.py
      ├── stage_redshift.py
      ├── load_fact.py
      ├── load_dimension.py
      └── data_quality.py
helpers/
  └── sql_queries.py
```

---

## ⚙️ Technologies Used
- Apache Airflow
- Amazon Redshift
- Amazon S3
- Python (custom operators)
- SQL (Redshift dialect)

---

## 🔁 Workflow Steps

1. `Begin_execution` – Starts the DAG
2. `Stage_events`, `Stage_songs` – Loads raw JSON from S3 to Redshift
3. `Load_songplays_fact_table` – Inserts data into fact table using SQL
4. `Load_user/song/artist/time_dim_table` – Loads dimension tables
5. `Run_data_quality_checks` – Verifies row counts in key tables
6. `Stop_execution` – Ends the DAG

---

## 🔌 Airflow Connections

Ensure the following Airflow connections are configured:

| ID               | Type         | Notes                        |
|------------------|--------------|-------------------------------|
| `aws_credentials` | Amazon Web Services | For accessing S3              |
| `redshift`        | Postgres     | Points to your Redshift cluster |

Also set this **Airflow Variable**:
```bash
s3_bucket = zainab-dend-buckets
```

---

## 🧪 Data Quality Checks
The DAG includes a custom operator that runs SQL checks such as:
```sql
SELECT COUNT(*) FROM users
SELECT COUNT(*) FROM songs
```
If results do not match expected values, the DAG will fail.

---

## 📄 Example SQL Logic

SQL logic is stored in `sql_queries.py`:
```sql
SELECT DISTINCT userid, firstname, lastname FROM staging_events WHERE page='NextSong';
```

---

## ✅ Rubric Coverage
- [x] Custom operators with parameters
- [x] Dynamic S3 → Redshift COPY logic
- [x] Configurable truncate vs append mode
- [x] Data quality tests with error handling
- [x] Fully defined DAG with dependencies

---

## Author
Zainab Abbas  
WGU D608: Data Pipelines
