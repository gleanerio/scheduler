from dagster import asset, get_dagster_logger, define_asset_job, ConfigurableResource
from dagster_aws.s3 import  S3Resource

#from dagster import Field
from pydantic import Field

from ..utils import PythonMinioAddress


class gleanerS3Resource(ConfigurableResource):
    # this should be s3, since it is the s3 resource. Others at gleaner s3 resources
    s3: S3Resource
    GLEANERIO_MINIO_BUCKET: str =  Field(
         description="GLEANERIO_MINIO_BUCKET.")
    GLEANERIO_MINIO_ADDRESS: str =  Field(
         description="GLEANERIO_MINIO_BUCKET.")
    GLEANERIO_MINIO_PORT: str =  Field(
         description="GLEANERIO_MINIO_BUCKET.")
    GLEANERIO_MINIO_USE_SSL: bool=  Field(
         default=False)
    GLEANERIO_CONFIG_PATH : str =  Field(
         description="GLEANERIO_CONFIG_PATH.", default="scheduler/configs/")
    GLEANERIO_TENANT_FILENAME : str =  Field(
         description="GLEANERIO_TENANT_FILENAME.", default="tenant.yaml")
    GLEANERIO_SOURCES_FILENAME: str =  Field(
         description="GLEANERIO_SOURCES_FILENAME.", default="gleanerconfig.yaml")
    # now using the boto s3 embedded in dagster_aws, but just in case we need them
    GLEANERIO_MINIO_ACCESS_KEY: str = Field(
        description="GLEANERIO_MINIO_ACCESS_KEY")
    GLEANERIO_MINIO_SECRET_KEY: str = Field(
        description="GLEANERIO_MINIO_SECRET_KEY")

    ## https://docs.dagster.io/_apidocs/libraries/dagster-a
# Courtesy method for the ec utilities
    def MinioOptions(self):
        return  {"secure": self.s3.use_ssl

            , "access_key":  self.s3.aws_access_key_id
            , "secret_key": self.s3.aws_secret_access_key
                         }
## https://docs.dagster.io/_apidocs/libraries/dagster-aws#s3
#   fields from dagster_aws.s3.S3Resource
# region_name
# endpoint_url
# use_ssl
# aws_access_key_id
# aws_secret_access_key
    def listPath(self, path='orgs', recusrsive=True):
        result = self.s3.get_client().list_objects(
            Bucket=self.GLEANERIO_MINIO_BUCKET,
            Prefix=path,
#            Recusrsive=recusrsive
        )
        return result["Contents"]
    def getFile(self, path='test'):
        try:
            result =  self.s3.get_client().get_object(
                Bucket=self.GLEANERIO_MINIO_BUCKET,
                Key=path,
            )
            get_dagster_logger().info(
                f"file {result['Body']}" )
            return result["Body"]
        except Exception as ex:
            get_dagster_logger().info(f"file {path} not found  in {self.GLEANERIO_MINIO_BUCKET} at {self.s3.endpoint_url} {ex}")
    def getTennatFile(self, path=''):
        if path == '':
            path= f"{self.GLEANERIO_CONFIG_PATH}{self.GLEANERIO_TENANT_FILENAME}"
        try:
            get_dagster_logger().info(f"tenant_path {path} ")
            return self.getFile( path=path)

        except Exception as ex:
            get_dagster_logger().info(f"tenant {path} not found ")
     #endpoint_url =_pythonMinioAddress(GLEANER_MINIO_ADDRESS, port=GLEANER_MINIO_PORT)

    # this will change to use just a sources.
    def getSourcesFile(self, path=''):
        if path == '':
            path= f"{self.GLEANERIO_CONFIG_PATH}{self.GLEANERIO_SOURCES_FILENAME}"
        try:
            get_dagster_logger().info(f"sources_path {path} ")
            return self.getFile( path=path)

        except Exception as ex:
            get_dagster_logger().info(f"sources_path {path} not found ")
     #endpoint_url =_pythonMinioAddress(GLEANER_MINIO_ADDRESS, port=GLEANER_MINIO_PORT)
