from aws_cdk import (
    Stage,
    aws_sagemaker as sagemaker,
    aws_iam as iam
)
from constructs import Construct

class ModelDeployStage(Stage):
    def __init__(self, scope: Construct, id: str, model_artifact_url: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # SageMaker Role to access model artifact
        execution_role = iam.Role(self, "SageMakerExecRole",
                              assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
                              managed_policies=[
                                  iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess"),
                                  iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"),
                              ]
                            )
    
        # SageMaker Model
        model = sagemaker.CfnModel(self, "Model",
                               execution_role_arn=execution_role.role_arn,
                               primary_container=sagemaker.CfnModel.ContainerDefinitionProperty(
                                   image="683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:1.0-1",
                                   model_data_url=model_artifact_url
                                 )
                                )
        
        # Endpoint Config
        endpoint_config = sagemaker.CfnEndpointConfig(self, "EndpointConfig",
                                                      production_variants=[sagemaker.CfnEndpointConfig.ProductionVariantProperty(
                                                          initial_instance_count=1,
                                                          instance_type="ml.m5.large",
                                                          model_name=model.attr_model_name,
                                                          variant_name="AllTraffic"
                                                      )]
                                                    )
        
        # Endpoint
        sagemaker.CfnEndpoint(self, "Endpoint",
                              endpoint_config_name=endpoint_config.attr_endpoint_config_name,
                              endpoint_name="mlops-realtime-endpoint")