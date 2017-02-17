# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:19:37 2015

@author: JunjieLiao
"""

import re

fileIn = open("regex_sum_180057.txt", 'r')
x = fileIn.read()
y = re.findall('[0-9]+', x)
ans = 0
for num in y:
    ans += int(num)
print ans