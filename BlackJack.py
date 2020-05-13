# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:29:41 2020

@author: Unmesh
"""


def blackjack(playerOrDealer,playersBlackJackValue,*args):
    if playersBlackJackValue == 21:
        return(playerOrDealer, playersBlackJackValue, 'Winner !! Winner Chicken Dinner.... You hit the BlackJack',*args)
    elif playersBlackJackValue <21:
        return(playerOrDealer, playersBlackJackValue,  'Compare with dealer',*args)
    
    elif playersBlackJackValue >21: 
        
        print('Inside Bust, Checking to see if A card is an Ace to reduce its value from 11 to 1')
        for everyBrokenTuple in args:
            for everyCard in everyBrokenTuple:
                if everyCard.rank == 'A':
                    playersBlackJackValue += -10
                    print(everyCard.suit , ' ',everyCard.rank)
                 
            if playersBlackJackValue > 21 :
                return(playerOrDealer,playersBlackJackValue, 'Bust',*args)
            else:
                return(playerOrDealer,playersBlackJackValue, 'Compare with dealer', *args)