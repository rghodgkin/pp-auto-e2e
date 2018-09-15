import os

class TopoTemps(object):
    sdn = {'name':'', 'network_list':[]}
    network = {'name':'', 'sdn_description':'', 'sdn_account': '', \
               'sdn_network_type': '', 'sdn_zone': '', 'edge_list':[]}
    cloud = {'name':'', 'sdn_description':'', 'sdn_network':'', \
             'sdn_cloud_provider':'', 'aws_cloud_region':'', \
             'sdn_cloud_location':'', 'aws_cloud_account':'', \
             'IPv4_CIDR_block':'', 'type':'cloud'} 
    site = {'name':'', 'sdn_description':'', \
            'sdn_network':'', 'sdn_zone':'', 'type':'site'}
    mobile = {'name':'', 'sdn_description':'', \
            'sdn_network':'', 'sdn_zone':'', 'type':'mobile'}
           
class SDNNetTrans(object):
    aws = {'us-east-1':'Ashburn, VA', \
           'us-west-1':'San Jose, CA', \
           'x':'Seattle, WA'}

class SDNCloudTrans(object):
    aws = {'us-east-2':'US East (Ohio)', \
           'us-east-1':'AWS US-East N Virginia', \
           'us-west-1':'AWS US-West N California', \
           'us-west-2':'AWS US-West Oregon'}  

class SDNSiteTrans(object):
    aws = {'us-east-1':'Ashburn, VA', \
           'us-west-1':'San Jose, CA', \
           'x':'Seattle, WA'} 

class AwsVpc(object):
    VPC_SUP_IP = '10.0.0.0'
    VPC_SUP_MASK = '8'
    VPC_SUB_PREFIX = '16'

