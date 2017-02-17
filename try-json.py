# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:41:45 2015

@author: JunjieLiao
"""

import urllib
import json

sample = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json"
act = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_180063.json"

#url = sample
url = act

data = urllib.urlopen(url).read()
info = json.loads(data)

ans = 0
for i in range(len(info['comments'])):
    ans += info['comments'][i]['count']
print ans
    