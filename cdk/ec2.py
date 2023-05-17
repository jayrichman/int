from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class ComputeStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ami = ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2)

        ec2.Instance(self, "Instance",
                     instance_type=ec2.InstanceType("t3.micro"),
                     machine_image=ami,
                     vpc = vpc,
                     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC))
