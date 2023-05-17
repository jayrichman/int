from aws_cdk import (
    aws_s3 as s3,
    core
)

class S3Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self, "Bucket",
                  bucket_name="int-test",
                  removal_policy=core.RemovalPolicy.DESTROY)
