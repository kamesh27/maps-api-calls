# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:08:33 2018

@author: Kamesh K S
"""

import urllib.request
import json
inputType = 'textquery'
endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
search_key = input('What do you want to search for?: ').replace('','+')
api_key=input('Enter your API Key: ').replace('','+')
search_req ='input={}&key={}'.format(search_key,api_key)
request = endpoint+search_req
response = urllib.request.urlopen(request).read()
output = json.loads(response)
print(output)