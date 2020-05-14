# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:31:48 2020

@author: Unmesh
"""



def declareResult(playersBlackJack,playersCards,dealersBlackJack,dealersCards,PlayersBet):
    print('Dealers Cards are:')
    for everyCard in dealersCards:
        print(everyCard.suit, ' ', everyCard.rank)
    
    
    print('\nPlayers Cards are: ')
    for everyCard in playersCards:
        print(everyCard.suit, ' ', everyCard.rank )
    
    print('\n', dealersBlackJack[0],dealersBlackJack[1])
    print('\n', playersBlackJack[0],playersBlackJack[1])
    
    dealersTotal = dealersBlackJack[1]
    
    playersTotal = playersBlackJack[1]
    
    if (playersTotal > dealersTotal and playersTotal <= 21):
        print('Players beats dealer')
        PlayersBet.updateBalance(PlayersBet.bet)
        
    elif (playersTotal < dealersTotal and dealersTotal <=21):
        print('Dealer beats Player')
        PlayersBet.updateBalance((PlayersBet.bet)*-1)
          
    elif (playersTotal <=21 and dealersTotal <=21 and playersTotal == dealersTotal):
        print('Both dealer and Player have same hand value. Its a push')
        
    elif (playersTotal <=21 and dealersTotal>21):
        print('Dealer goes bust. Player wins')
        PlayersBet.updateBalance(PlayersBet.bet)
    elif (playersTotal >21 and dealersTotal <=21):
        print('Player goes bust. Dealer wins')
        PlayersBet.updateBalance((PlayersBet.bet)*-1)
        
    
    
    #Check if player hit BlackJack
    #Check if dealer hit BlackJack
    #Check if player went bust
    #Check if dealer went bust
    
    #Check if both are equal
    #Check if Player beat dealer
    #Check if Player lost to dealer
    
