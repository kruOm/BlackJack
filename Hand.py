# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:14:48 2020

@author: Unmesh
"""


class Hand():
    
    def __init__(self,deck,popIndex):
        self.deck = deck
        self.popIndex = popIndex
        self.CardinHand = deck[popIndex]
        deck.pop(popIndex)