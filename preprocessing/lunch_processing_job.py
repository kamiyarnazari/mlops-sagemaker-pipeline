import sagemaker
import sagemaker.image_uris
from sagemaker.processing import ScriptProcessor, ProcessingInput, ProcessingOutput
import boto3


# Configuration
region = "us-east-1"
account_id = boto3.client("sts").get_caller_identity()["Account"]

role_arn = "arn:aws:iam::906929958324:role/MlopsCdkStack-SageMakerExecutionRole7843F3B8-GPaAgARZgBFB"
raw_bucket = "mlopscdkstack-rawdatabucket57f26c03-ztwurisscq78"
processed_bucket = "mlopscdkstack-processeddatabucket4e25d3b7-edpjdvxuudxl"
script_path = "preprocessing/preprocess.py"

# Setup
sagemaker_session = sagemaker.Session()
processor = ScriptProcessor(
    image_uri=sagemaker.image_uris.retrieve("sklearn", region, version="1.0-1"),
    role=role_arn,
    instance_count=1,
    instance_type="ml.t3.medium",
    command=["python3"],
    sagemaker_session=sagemaker_session
)

# Run the job
processor.run(
    code=script_path,
    inputs=[
        ProcessingInput(
            source=f"s3://{raw_bucket}/data.csv",
            destination="/opt/ml/processing/input"
        )
    ],
    outputs=[
        ProcessingOutput(
            source="/opt/ml/processing/output",
            destination=f"s3://{processed_bucket}/"
        )
    ]
)
