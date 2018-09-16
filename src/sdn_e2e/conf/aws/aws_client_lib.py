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
                                   CidrBlock=cidr)
        return 1, output
    except:
        logging.error("create_aws_subnet: Failed to provision \
            subnet")
        return 0, {}

def create_aws_ig(region, vpcid):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        output = ec2.create_internet_gateway()
        #output['InternetGateway']['Attachments'][0]['VpcId'] = vpcid
        igw_id = output['InternetGateway']['InternetGatewayId'] 
        output2 = ec2.attach_internet_gateway(InternetGatewayId=igw_id, 
                                    VpcId=vpcid)
        return 1, output

    except:
        logging.error("create_aws_ig: Failed to provision \
            Internet Gateway")
        return 0, {}

def create_aws_vg(region, az, vpcid, bgpasn=64512):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        output = ec2.create_vpn_gateway(AvailabilityZone=az,
                                        Type='ipsec.1',
                                        AmazonSideAsn=bgpasn)
        vgw_id = output['VpnGateway']['VpnGatewayId']
        output2 = ec2.attach_vpn_gateway(VpcId=vpcid,
                                    VpnGatewayId=vgw_id)
        return 1, output

    except:
        logging.error("create_aws_vg: Failed to provision \
            Virtual Private Gateway")
        return 0, {}

def create_aws_route(region, rtid, cidr, igwid):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        output = ec2.create_route(DestinationCidrBlock=cidr,
                                  GatewayId=igwid,
                                  RouteTableId=irtid)
        return 1, output
    except:
        logging.error("create_aws_route: Failed to provision \
            route AWS routing table")
        return 0, {} 

def describe_aws_region(region):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_regions()
        return response
    except:
        logging.error("Error: describe_aws_region failed to describe regions")

def describe_aws_az(region):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_availability_zones()
        return response
    except:
        logging.error("Error: describe_aws_region failed to describe AZ's")





    
