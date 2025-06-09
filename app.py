#!/usr/bin/env python3
import os

import aws_cdk as cdk

from mlops_cdk.mlops_cdk_stack import MlopsCdkStack

env = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION")
)

app = cdk.App()
MlopsCdkStack(app, "MlopsCdkStack", env=env)
app.synth()
