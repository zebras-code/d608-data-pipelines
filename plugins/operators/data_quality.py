# plugins/operators/data_quality.py
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DataQualityOperator(BaseOperator):
    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 tests=None,
                 *args, **kwargs):
        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tests = tests or []

    def execute(self, context):
        self.log.info(f"Running data quality checks using Redshift connection: {self.redshift_conn_id}")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        for test in self.tests:
            query = test.get("table")
            expected = test.get("return")
            self.log.info(f"Running test: {query}, expecting result: {expected}")

            result = redshift.get_records(query)

            if len(result) < 1 or result[0][0] != expected:
                error_msg = f"❌ Data quality check failed: {query} returned {result[0][0]}, expected {expected}"
                self.log.error(error_msg)
                raise ValueError(error_msg)
            else:
                self.log.info(f"✅ Passed: {query} returned expected result {expected}")

        self.log.info("✅ All data quality checks passed.")
