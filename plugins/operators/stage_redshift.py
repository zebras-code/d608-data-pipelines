# plugins/operators/stage_redshift.py
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook


class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    template_fields = ('s3_path',)

    copy_sql = """
        COPY {table}
        FROM '{s3_path}'
        ACCESS_KEY_ID '{access_key}'
        SECRET_ACCESS_KEY '{secret_key}'
        FORMAT AS JSON '{json_option}';
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 table="",
                 s3_path="",
                 json_option="auto",
                 *args, **kwargs):
        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.table = table
        self.s3_path = s3_path
        self.json_option = json_option

    def execute(self, context):
        self.log.info(f"Staging data from {self.s3_path} to Redshift table {self.table}")

        aws_hook = AwsBaseHook(self.aws_credentials_id, client_type='sts')
        credentials = aws_hook.get_credentials()

        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        redshift.run(f"DELETE FROM {self.table}")

        formatted_sql = StageToRedshiftOperator.copy_sql.format(
            table=self.table,
            s3_path=self.s3_path,
            access_key=credentials.access_key,
            secret_key=credentials.secret_key,
            json_option=self.json_option
        )

        self.log.info(f"Running COPY command:")
        self.log.info(formatted_sql)
        redshift.run(formatted_sql)

        self.log.info(f"✅ Successfully staged {self.table}")
