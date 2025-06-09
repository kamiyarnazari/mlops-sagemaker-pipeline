from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3
)
from constructs import Construct

class MlopsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "RawDataBucket",
                  versioned=True,
                  removal_policy=RemovalPolicy.DESTROY)
