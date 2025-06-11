from sagemaker.sklearn.estimator import SKLearn
from sagemaker.inputs import TrainingInput
import sagemaker
import os
from datetime import datetime

job_name = f"rf-model-train-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

role = role = "arn:aws:iam::906929958324:role/MlopsCdkStack-SageMakerExecutionRole7843F3B8-GPaAgARZgBFB"
session = sagemaker.Session()

bucket = "mlopscdkstack-processeddatabucket4e25d3b7-edpjdvxuudxl"

# Define the estimator
sklearn_estimator = SKLearn(
    entry_point="train.py",
    source_dir="training",
    role=role,
    instance_type="ml.m5.large",
    framework_version="1.2-1",
    py_version="py3",
    base_job_name="rf_model_train",
    sagemaker_session=session
)

# Run this job
sklearn_estimator.fit(
    {
    "train": TrainingInput(
        s3_data=f"s3://{bucket}/cleaned.csv",
        content_type="csv"
    )
    },
    job_name=job_name
)