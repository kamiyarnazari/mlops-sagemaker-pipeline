import aws_cdk as core
import aws_cdk.assertions as assertions

from mlops_cdk.mlops_cdk_stack import MlopsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in mlops_cdk/mlops_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MlopsCdkStack(app, "mlops-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
