# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:21:44 2020

@author: Unmesh
"""
import checkIfFaceOrNumber as modulecheckIfFaceOrNumber


class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = modulecheckIfFaceOrNumber.checkIfFaceOrNumber(rank)
        
    def printCard(self):
        print("You are holding a ",self.rank, " of", self.suit, 'with a value of', self.value)

