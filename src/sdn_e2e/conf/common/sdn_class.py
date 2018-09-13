#!/usr/bin/env python
# encoding: utf-8

import logging
import yaml
import pdb

class SdnNetObj(object):
    def __init__(self, config_dict):
        self.config = config_dict
        self.edge_cloud_list = []
        self.edge_site_list = []
        self.edge_mobile_list = []
        self.gen_edge_data()

    def gen_edge_data(self):
        '''
        This method is going to parse the self.config and create
         all edge objects, passing in edge specific dict info
        '''
        logging.info("Inside gen_edge_data") 
        logging.info("Config data is: %s" % self.config)

class SdnEdgeParent(object):
    def __init__(self, config_dict):
        self.config = config_dict

class SdnEdgeCloudObj(SdnEdgeParent):
    def __init__(self, config_dict):
        SdnEdgeParent.__init__(self, config_dict )

    def sdn_deploy(self):
        pass

    def sdn_destroy(self):
        pass

    def aws_deploy(self):
        pass 

    def aws_destroy(self):
        pass 

class SdnEdgeSiteObj(SdnEdgeParent):
    def __init__(self, config_dict):
        SdnEdgeParent.__init__(self, config_dict ) 

    def sdn_deploy(self):
        pass

    def sdn_destroy(self):
        pass

class SdnEdgeMobleObj(SdnEdgeParent):
    def __init__(self, config_dict):
        SdnEdgeParent.__init__(self, config_dict )

    def sdn_deploy(self):
        pass

    def sdn_destroy(self):
        pass

        

