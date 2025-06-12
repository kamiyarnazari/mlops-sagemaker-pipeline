import boto3

# Initilize the SageMaker runtime client
runtime = boto3.client("sagemaker-runtime")

endpoint_name = "mlops-realtime-endpoint"

# A random input same as data CSV structure
test_input = "28.0,42.0"

# Invoke endpoint
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="text/csv",
    Body=test_input
)

# Print the prediction
result = response["Body"].read().decode("utf-8")
print("prediction", result)