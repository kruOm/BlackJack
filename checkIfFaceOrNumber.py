# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:56:46 2020

@author: Unmesh
"""


def checkIfFaceOrNumber(valueOfRank):
    try:
        int(valueOfRank)
    except :
        if valueOfRank == 'A':
            valueOfRank = 11
        else: 
            valueOfRank = 10
    return(valueOfRank)