#!/usr/bin/env python3
import os
import aws_cdk as cdk
from pipeline_stack import MLOpsPipelineStack

env = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION")
)

app = cdk.App()
MLOpsPipelineStack(app, "MLOpsPipelineStack", env=env)
app.synth()
