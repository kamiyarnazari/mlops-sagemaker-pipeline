import sagemaker
import sagemaker.session
from sagemaker.sklearn.model import SKLearnModel
import os

model_uri = "s3://sagemaker-us-east-1-906929958324/rf-model-train-2025-06-11-22-10-48/output/model.tar.gz"
role = "arn:aws:iam::906929958324:role/MlopsCdkStack-SageMakerExecutionRole7843F3B8-GPaAgARZgBFB"
entry_point = "deployment/inference.py"

# Initilize session
sagemaker_session = sagemaker.Session()

# Create the SKLearnModel
model = SKLearnModel(
    model_data=model_uri,
    role=role,
    entry_point=entry_point,
    framework_version="1.2-1",
    sagemaker_session=sagemaker_session
)

# Deploy to real-time endpoint
predictor = model.deploy(
    instance_type="ml.m5.large",
    initial_instance_count=1,
    endpoint_name="mlops-realtime-endpoint"
)