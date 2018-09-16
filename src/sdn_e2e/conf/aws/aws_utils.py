#!/usr/bin/env python
# encoding: utf-8

import logging
import yaml
import pdb
import sdn_e2e.conf.aws.aws_client_lib as aws
import sdn_e2e.conf.common.utils as utils

def deploy_aws_cloud(topo):
    # All AWS JSON output will be stored within aws_data{} dict and
    # returned back 
    aws_data = {}

    # 1. Deploy VPC
    result = aws.create_aws_vpc(topo['aws_cloud_region'], 
                                topo['IPv4_CIDR_block'])
    if result[0] == 1:
        aws_data['vpc'] = result[1] 
        topo['vpcid'] = aws_data['vpc']['Vpc']['VpcId']
    else:
        logging.error("deploy_aws_cloud: AWS provision of VPC failed")
        return 0, {} 

    # 2. Deploy subnet
    topo['ipv4_subnets']= utils.return_ip_subnets(str(topo['IPv4_CIDR_block']), 
                                24, skip_zero=True)
    #  By default we grab the first AZ in list of region
    az = aws.describe_aws_az(topo['aws_cloud_region'])['AvailabilityZones'][0]['ZoneName'] 
    result = aws.create_aws_subnet(topo['aws_cloud_region'],
                                   topo['vpcid'],
                                   az, 
                                   topo['ipv4_subnets'].pop())
    if result[0] == 1:
        aws_data['subnet'] = result[1]
        topo['ipv4_subnet1'] = {}
        topo['ipv4_subnet1']['ip_addr'] = aws_data['subnet']['Subnet']['CidrBlock']
        topo['ipv4_subnet1']['az'] = az
    else:
        logging.error("deploy_aws_cloud: AWS provision of IP Subnet failed")
        return 0, {}

    pdb.set_trace()



  

 
    return 1, aws_data

