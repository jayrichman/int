from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class NetworkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           cidr="10.0.0.0/16",
                           subnet_configuration=[
                                ec2.SubnetConfiguration(
                                    name="Public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                                ec2.SubnetConfiguration(
                                    name="Private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)
                           ])
