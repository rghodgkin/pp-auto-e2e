#!/usr/bin/python

import yaml
import pdb
import os
import logging

def import_yaml_to_dict(file):
    """
        This function takes a filename in yaml format and returns
         it as a dict type
    """
    try:
        f = open(file)
        data = yaml.safe_load(f)

    except:
        logging.error("import_yaml_to_dict: Issues importing yaml file")
        return 0, {}

    return 1, data 
    
     

