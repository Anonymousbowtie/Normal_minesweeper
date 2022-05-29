"""
Created on Wed Apr 27 18:15:36 2022

@author: ljhs8
"""

import settings

def height_pct(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_pct(percentage):
    return (settings.WIDTH / 100) * percentage
