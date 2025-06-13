from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_iam as iam
)
from constructs import Construct

class MlopsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.raw_data_bucket = s3.Bucket(self, "RawDataBucket",
                  versioned=True,
                  removal_policy=RemovalPolicy.DESTROY)
        
        # Processed data bucket
        self.processed_data_bucket = s3.Bucket(self, "ProcessedDataBucket",
                                               versioned=True,
                                              removal_policy=RemovalPolicy.DESTROY)
        
        # SageMaker execution role
        self.sagemaker_role = iam.Role(self, "SageMakerExecutionRole",
                                       assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
                                       description="Execution role for SageMaker Processing and Training Jobs")
        

        # Grant S3 access to SageMaker
        self.raw_data_bucket.grant_read_write(self.sagemaker_role)
        self.processed_data_bucket.grant_read_write(self.sagemaker_role)

        # Grant CloudWatch Logs permissions
        self.sagemaker_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess")
        )
