#!/usr/bin/env python
# encoding: utf-8

import logging
import pdb
import boto3

def create_aws_vpc(region, cidr):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        output = ec2.create_vpc(CidrBlock=cidr)
        return 1, output
    except:
        logging.error("create_aws_vpc: Failed to provision VPC")
        return 0, {}

def create_aws_subnet(region, vpcid, az, cidr):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        output = ec2.create_subnet(
            VpcId=vpcid,
            AvailabilityZone=az,
            CidrBlock=cidr
        return 1, output
    except:
        logging.error("create_aws_subnet: Failed to provision \
            subnet")
        return 0, {}
    
