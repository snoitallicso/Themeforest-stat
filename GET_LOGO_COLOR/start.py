# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:08:33 2018

@author: pow
"""
from pynche import ColorDB
import webcolors
import heapq
from PIL import Image
img = Image.open("13739153.png")
#colors = img.convert('RGB').getcolors()
colors = img.getcolors(img.size[0] * img.size[1])

#heapq.nlargest(2,[1,435,5634,34,23])
topcolors = heapq.nlargest(10, colors, key=lambda s: s[0])
print (topcolors)
for color in topcolors:
    rgb = color[1]
    r = rgb[0]
    g = rgb[1] 
    b = rgb[2]
    
    #print(color)
    print(colordb.nearest(r,g,b), rgb)
    
#webcolors.rgb_to_name([4,144,233])