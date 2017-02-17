# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 02:02:28 2015

@author: JunjieLiao
"""

import urllib
from BeautifulSoup import *

#part1
#sample = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html"
#act = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_180062.html"
#
##url = sample
#url = act
#html = urllib.urlopen(url).read()
#
#soup = BeautifulSoup(html)
#
## Retrieve all of the anchor tags
#ans = 0
#tags = soup('span')
#for tag in tags:
#   # Look at the parts of a tag
#   ans += int(tag.contents[0])
#print ans

sample = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Iria.html"
act = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Yassin.html"

#url = sample
url = act
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

count = int(raw_input("Enter count:"))
pos = int(raw_input("Enter position:"))

# Retrieve all of the anchor tags
for c in range(count):
    tags = soup('a')
    p = 0
    for tag in tags:
        if p < pos:
            url = tag.get('href', None)
            name = tag.contents[0]
            print name
            p += 1
        else:
            break
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)