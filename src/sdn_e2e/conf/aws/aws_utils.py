#!/usr/bin/env python
# encoding: utf-8

import logging
import yaml
import pdb
import sdn_e2e.conf.aws.aws_client_lib as aws

def deploy_aws_cloud(topo):
    # All AWS JSON output will be stored within aws_data{} dict and
    # returned back 
    aws_data = {}

    # 1. Deploy VPC
    result = aws.create_aws_vpc(topo['aws_cloud_region'], 
                                topo['IPv4_CIDR_block'])
    if result[0] == 1:
        aws_data['vpc'] = result[1] 

    # 2. Deploy subnet

 
    return aws_data

