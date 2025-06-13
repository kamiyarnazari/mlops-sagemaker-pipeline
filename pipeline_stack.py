from aws_cdk import Stack, SecretValue
from aws_cdk.pipelines import CodePipeline, ShellStep, CodePipelineSource
from constructs import Construct


class MLOpsPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)



        pipeline = CodePipeline(
            self, "MLOpsPipeline",
            pipeline_name="MLOpsSageMakerPipeline",
            synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("kamiyarnazari/mlops-sagemaker-pipeline",
                            "main",
                            authentication=SecretValue.secrets_manager("github_repo")
                            ),
                            commands=[
                            "npm install -g aws-cdk",
                            "python -m venv .venv",
                            ". .venv/bin/activate || .venv\\Scripts\\activate",  
                            "pip install -r requirements.txt",
                            "cdk synth"
                            ]

            )
        )