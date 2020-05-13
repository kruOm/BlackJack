# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:31:48 2020

@author: Unmesh
"""



def declareResult(playersBlackJack,playersCards,dealersBlackJack,dealersCards):
    print('Dealers Cards are:')
    for everyCard in dealersCards:
        print(everyCard.suit, ' ', everyCard.rank)
    
    
    print('\nPlayers Cards are: ')
    for everyCard in playersCards:
        print(everyCard.suit, ' ', everyCard.rank )
    
    print('\n', dealersBlackJack[0],dealersBlackJack[1])
    print('\n', playersBlackJack[0],playersBlackJack[1])
    
    #Check if player hit BlackJack
    #Check if dealer hit BlackJack
    #Check if player went bust
    #Check if dealer went bust
    
    #Check if both are equal
    
    #Check if Player beat dealer
    #Check if Player lost to dealer
    
