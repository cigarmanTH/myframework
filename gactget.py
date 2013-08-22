#!/usr/local/pythonz/ENV/Python-2.7.3/bin/python
# coding: utf-8 

import apiclient.discovery
import httplib2
import settings 
import logging
#logging.basicConfig()
logging.getLogger().setLevel(getattr(logging, 'ERROR'))

import ggtsidset

def build_service(credentials, http, api_key=None):
    if ( credentials != None ):
        http = credentials.authorize(http)
    service = apiclient.discovery.build('plus', 'v1', http=http, developerKey=api_key)
    return service

def gactget(ggtsid):

    httpUnauth = httplib2.Http()
    serviceUnauth = build_service(None, httpUnauth, settings.API_KEY)
    request = serviceUnauth.activities().list(userId=ggtsid, collection='public')
    
    activities = []
    
    activity = request.execute(httpUnauth)
    activities += activity['items']

    return activities