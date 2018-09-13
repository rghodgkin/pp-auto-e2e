import pytest
import logging
import pdb
import os
import yaml
import sdn_e2e.conf.common.logging_util as logging_util

pytest_plugins = [
    'sdn_e2e.fixtures.hook',
    'sdn_e2e.fixtures.common'
]

def pytest_addoption(parser):
    parser.addoption("--configfile", required=True, action="store",
                     default=None, help="Path to testcase config data file")
    parser.addoption("--topo", required=True, action="store",
                     default=None, help="Path to testcase topo data file")
    parser.addoption("--logfile", required=True, action="store",
                     default=None, help="Path to pytest log file")

def pytest_cmdline_main(config):
    log_file = config.getoption("--logfile")
    log_dir = os.path.dirname(log_file)
    os.system("mkdir -p %s" % log_dir)
    logging_util.init(log_file, "DEBUG")




