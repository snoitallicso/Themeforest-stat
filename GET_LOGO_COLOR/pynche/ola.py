# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:08:33 2018

@author: pow
"""
import ColorDB
import webcolors
import heapq
from PIL import Image
#img = Image.open("7758048.png")
#colors = img.convert('RGB').getcolors()
colors = img.getcolors(img.size[0] * img.size[1])

#heapq.nlargest(2,[1,435,5634,34,23])
#topcolors = heapq.nlargest(5, colors, key=lambda s: s[0])
#print (topcolors)
#webcolors.rgb_to_name([4,144,233])