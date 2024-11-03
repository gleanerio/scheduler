import yaml
from dagster import asset, get_dagster_logger, define_asset_job, ConfigurableResource
from dagster_aws.s3 import  S3Resource

#from dagster import Field
from pydantic import Field

def _pythonMinioAddress(url, port=None):
    if (url.endswith(".amazonaws.com")):
        PYTHON_MINIO_URL = "s3.amazonaws.com"
    else:
        PYTHON_MINIO_URL = url
    if port is not None:
        PYTHON_MINIO_URL = f"{PYTHON_MINIO_URL}:{port}"
    return PYTHON_MINIO_URL


class gleanerS3Resource(ConfigurableResource):
    s3: S3Resource
    GLEANERIO_MINIO_BUCKET: str =  Field(
         description="GLEANERIO_MINIO_BUCKET.")
    GLEANERIO_MINIO_ADDRESS: str =  Field(
         description="GLEANERIO_MINIO_BUCKET.")
    GLEANERIO_MINIO_PORT: str =  Field(
         description="GLEANERIO_MINIO_BUCKET.")
    GLEANERIO_MINIO_USE_SSL: bool = Field(
         default=False)
    GLEANERIO_CONFIG_PATH : str =  Field(
         description="GLEANERIO_CONFIG_PATH.", default="scheduler/configs/test/")
    GLEANERIO_TENANT_FILENAME : str =  Field(
         description="GLEANERIO_TENANT_CONFIG.", default="tenant.yaml")
    # now using the boto s3 embedded in dagster_aws, but just in case we need them
    GLEANERIO_MINIO_ACCESS_KEY: str =  Field(
         description="GLEANERIO_MINIO_ACCESS_KEY")
    GLEANERIO_MINIO_SECRET_KEY: str =  Field(
         description="GLEANERIO_MINIO_SECRET_KEY")
## https://docs.dagster.io/_apidocs/libraries/dagster-aws#s3
#   fields from dagster_aws.s3.S3Resource
# region_name
# endpoint_url
# use_ssl
# aws_access_key_id
# aws_secret_access_key
    def listPath(self, path='orgs'):
        return self.s3.get_client().list_objects(
            Bucket=self.GLEANERIO_MINIO_BUCKET,
            Prefix=path,

        )["Contents"]

    def getTennatInfo(self, path='orgs'):
        path= f"{self.GLEANERIO_CONFIG_PATH}{self.GLEANERIO_TENANT_FILENAME}"
        try:
            r =  self.s3.get_client().get_object(
                Bucket=self.GLEANERIO_MINIO_BUCKET,
                Key=path,
            )
            return  yaml.safe_load(r["Body"])
        except Exception as ex:
            get_dagster_logger().info(f"tennant file {path} not found in bucket {self.GLEANERIO_MINIO_BUCKET} at {self.GLEANERIO_MINIO_ADDRESS} ")
            raise ex
     #endpoint_url =_pythonMinioAddress(GLEANER_MINIO_ADDRESS, port=GLEANER_MINIO_PORT)
