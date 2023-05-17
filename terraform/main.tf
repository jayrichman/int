resource "aws_instance" "test1" {
  ami           = var.ubuntu_ami_id
  instance_type = var.instance_type
  subnet_id     = module.vpc.public_subnets[0]

  ebs_block_device {
    device_name = "/dev/sda1"
    volume_size = "20"
  }
  tags = local.tags
}

resource "aws_instance" "test2" {
  ami           = var.ubuntu_ami_id
  instance_type = var.instance_type
  subnet_id     = module.vpc.public_subnets[1]

  ebs_block_device {
    device_name = "/dev/sda1"
    volume_size = "20"
  }
  tags = local.tags
}