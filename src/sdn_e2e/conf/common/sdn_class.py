#!/usr/bin/env python
# encoding: utf-8

import logging
import yaml
import pdb

class SdnNetObj(object):
    def __init__(self, topo_dict, common):
        self.topo = topo_dict
        self.common = common
        self.edge_cloud_list = []
        self.edge_site_list = []
        self.edge_mobile_list = []
        self.gen_edge_data()

    def gen_edge_data(self):
        '''
        This method is going to parse the self.config_dict and create
         all edge objects, passing in edge specific dict info
        '''
        logging.info("Inside gen_edge_data") 
        logging.info("Topo data is: %s" % self.topo)

        for edge_item in self.topo['edge_list']:
            self.create_edge_inst(edge_item['type'], edge_item)
        
    def create_edge_inst(self, type, topo_dict):
        if type == "cloud":
            tmp_obj = SdnEdgeCloudObj(topo_dict, self.common)
            self.edge_cloud_list.append(tmp_obj) 

        elif type == "site":
            tmp_obj = SdnSiteCloudObj(topo_dict, self.common)
            self.edge_site_list.append(tmp_obj) 

        elif type == "mobile":
            tmp_obj = SdnMobileCloudObj(topo_dict, self.common)
            self.edge_mobile_list.append(tmp_obj) 
        

class SdnEdgeParent(object):
    def __init__(self, topo_dict, common):
        self.topo = topo_dict
        self.common = common

class SdnEdgeCloudObj(SdnEdgeParent):
    def __init__(self, topo_dict, common):
        SdnEdgeParent.__init__(self, topo_dict, common)

    def sdn_deploy(self):
        pass

    def sdn_destroy(self):
        pass

    def aws_deploy(self):
        pass 

    def aws_destroy(self):
        pass 

class SdnEdgeSiteObj(SdnEdgeParent):
    def __init__(self, topo_dict, common):
        SdnEdgeParent.__init__(self, topo_dict, common) 

    def sdn_deploy(self):
        pass

    def sdn_destroy(self):
        pass

class SdnEdgeMobileObj(SdnEdgeParent):
    def __init__(self, topo_dict, common):
        SdnEdgeParent.__init__(self, topo_dict, common)

    def sdn_deploy(self):
        pass

    def sdn_destroy(self):
        pass

        

