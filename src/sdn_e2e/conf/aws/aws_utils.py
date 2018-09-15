#!/usr/bin/env python
# encoding: utf-8

import logging
import yaml
import pdb
import sdn_e2e/conf/aws/aws_client_lib as aws

def deploy_aws_cloud(aws_data, topo):
    # aws_data is being passed as value and thus the below
    #   is setting the actual data in object 
    # 1. Deploy VPC
    aws_data['vpc'] = aws.create_aws_vpc(
                      topo['aws_cloud_region'],
                      topo['IPv4_CIDR__block'])
 
    return aws_data

