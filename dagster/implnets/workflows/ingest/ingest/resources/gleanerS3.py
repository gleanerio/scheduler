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
    GLEANERIO_TENNANT_PATH : str =  Field(
         description="GLEANERIO_TENNANT_CONFIG.", default="scheduler/configs/")
    GLEANERIO_TENNANT_FILENAME : str =  Field(
         description="GLEANERIO_TENNANT_CONFIG.", default="tennant.yaml")

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
            return result["Contents"]
        except Exception as ex:
            get_dagster_logger().info(f"file {path} not found  in {self.GLEANERIO_MINIO_BUCKET} at ")
    def getTennatFile(self, path='orgs'):
        path= f"{self.GLEANERIO_TENNANT_PATH}{self.GLEANERIO_TENNANT_FILENAME}"
        try:
            return self.s3.getFile(self, path=path)

        except Exception as ex:
            get_dagster_logger().info(f"tennant not found ")
     #endpoint_url =_pythonMinioAddress(GLEANER_MINIO_ADDRESS, port=GLEANER_MINIO_PORT)
