# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:51:37 2015

@author: JunjieLiao
"""

import urllib
import json

googleURL = "http://maps.googleapis.com/maps/api/geocode/json?"

address = raw_input("Enter location: ")
googleURL += urllib.urlencode({'sensor': 'false', 'address': address})

data = urllib.urlopen(googleURL).read()
info = json.loads(data)

#print json.dumps(info, indent = 4)

print info['results'][0]['place_id']