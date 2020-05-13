# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:53:59 2020

@author: Unmesh
"""


import random
from Card import Card

def generateDeck(suit,rank,deck):
    for everyItem in suit:
        for everyRank in rank:
            deck.append(Card(everyItem,everyRank))
    return(deck)


def printDeck(deck):
    for everyCard in deck:
        print(everyCard.suit, " ", everyCard.rank, ' ', everyCard.value)

def printCard(*args):
    if type(args) == tuple:
        for everyCard in args:
            print(everyCard.suit, ' ', everyCard.rank, ' ', everyCard.value)
    elif type(args) == list:
        for everyCard in args:
           print(everyCard)
            #print(everyCard.suit, ' ', everyCard.rank, ' ', everyCard.value)
    else:
        print(args.suit, ' ', args.rank, ' ', args.value)
        
def shuffleDeck(deck):
    for x in range(0,100,1):
        random.shuffle(deck)    
    return(deck)

def pickCard(deck,popIndex):
    returnCard = deck[popIndex]
    deck.pop(popIndex)
    return(returnCard)