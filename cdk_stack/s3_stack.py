from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_lambda as lm
)
from constructs import Construct

class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    # Create an Amazon S3 bucket
        s3_bucket_image = s3.Bucket(self, "dtdjimage",bucket_name="dtdj-build-image",
                              removal_policy=RemovalPolicy.DESTROY,
                              auto_delete_objects=True)
        
        s3_bucket_logs = s3.Bucket(self, "dtdjlogs",bucket_name="dtdj-build-logs",
                              removal_policy=RemovalPolicy.DESTROY,
                              auto_delete_objects=True)