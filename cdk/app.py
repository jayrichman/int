from aws_cdk import core

from vpc import NetworkStack
from ec2 import ComputeStack
from s3 import S3Stack

app = core.App()

network_stack = NetworkStack(app, "NetworkStack")
compute_stack = ComputeStack(app, "ComputeStack", vpc=network_stack.vpc)
s3_stack = S3Stack(app, "S3Stack")

app.synth()
