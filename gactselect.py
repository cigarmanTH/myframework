#bin/python
# coding: utf-8

# at first time in new environment,run plus_cli.py to get credentials before run this script
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

import apiclient.discovery
import httplib2
import settings

import logging
#logging.basicConfig()
logging.getLogger().setLevel(getattr(logging, 'ERROR'))
import pymongo

from pymongo import Connection
con = Connection('27.120.110.77', 27017)
db = con.sns
col = db.ggts
if __name__=='__main__':
    activities = col.find()
    for activity in activities: 
        print activity

