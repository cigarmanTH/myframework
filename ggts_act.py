#! c:/Python26/python.exe
# coding: utf-8 

# at first time in new environment,run plus_cli.py to get credentials before run this script
import sys
import codecs
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

import apiclient.discovery
import httplib2
import settings 
import simplejson as json

import logging
#logging.basicConfig()
logging.getLogger().setLevel(getattr(logging, 'ERROR'))

import ggtsidset

def build_service(credentials, http, api_key=None):
    if ( credentials != None ):
        http = credentials.authorize(http)
    service = apiclient.discovery.build('plus', 'v1', http=http, developerKey=api_key)
    return service

def activityprint(ggtsid):

    httpUnauth = httplib2.Http()
    serviceUnauth = build_service(None, httpUnauth, settings.API_KEY)
    request = serviceUnauth.activities().list(userId=ggtsid, collection='public')
    
    activities = []
    
    activity = request.execute(httpUnauth)
    activities += activity['items']
    
    if len(activities) > 0:
        for item in activities:
            item['_id'] = item['id'] 
            pp(item)

def pp(obj):
    if isinstance(obj, list) or isinstance(obj, dict):
        orig = json.dumps(obj, indent=4)
#        orig = json.dumps(obj)
        print eval("u'''%s'''" % orig).encode('utf-8')
    else:
        print obj
        
if __name__=='__main__':
    for ggtsid in ggtsidset.ggtsids:
        activityprint(ggtsid)
