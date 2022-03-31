# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:51:27 2015

"""

import urllib
import xml.etree.ElementTree as ET

sample = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml"
act = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_180059.xml"

#url = sample
url = act

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('comments')
ans= 0

lst = results[0].findall('comment')
for i in range(len(lst)):
    ans += int(lst[i].find('count').text)
print ans
