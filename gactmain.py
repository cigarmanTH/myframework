#!bin/python
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

import ggtsidset
import gactget

if __name__=='__main__':
    for ggtsid in ggtsidset.ggtsids:
        activities = gactget.gact(ggtsid)
        for activity in activities:
            print activity['published']
            print activity['updated']
            print activity['actor']['displayName']
            print activity['actor']['id']
            print activity['object']['content']
            print activity['object']['attachments'][0]['url']
            print activity['object']['replies']['totalItems']
            print activity['object']['plusoners']['totalItems']
            print activity['object']['resharers']['totalItems']
