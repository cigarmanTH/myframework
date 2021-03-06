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

def searchprint(keyword):

    httpUnauth = httplib2.Http()
    serviceUnauth = build_service(None, httpUnauth, settings.API_KEY)
    request = serviceUnauth.activities().search(query=keyword,maxResults=2 )
    results = []
    while ( request != None ):
        try:
            result = request.execute(httpUnauth)
            if 'items' in result:
                results += result['items']
                request = serviceUnauth.activities().list_next(request, result)
        except:
            print 'serviceUnauth error'
            print sys.exc_info()[:2]
#            return
            continue

if __name__=='__main__':
    keyword = 'Tomoyoshi'
    searchprint(keyword)
