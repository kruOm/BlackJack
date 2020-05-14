# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:23:32 2020

@author: Unmesh
"""
import playersEngine as engineModule
import declareResult as declareResultModule

def playAgain(PlayersBet, deck,popIndex):

    PlayersBet.bet = int(input('Place your bets please ? $'))  
    while PlayersBet.bet <= PlayersBet.cashBalance and PlayersBet.cashBalance>0: 
        
        (dealersBlackJack, popIndex, deck) = engineModule.dealersEngine('Dealer',deck, popIndex)
    
    
        (playersBlackJack, popIndex, deck) = engineModule.playersEngine('Player',deck, popIndex)
        
        
        
        
        (playersBlackJack, popIndex, playersCards, deck) = engineModule.playersEngineGamblingTime(playersBlackJack,deck,popIndex)
        (dealersBlackJack, popIndex, dealersCards, deck ) = engineModule.dealersGamblingTime(dealersBlackJack,deck,popIndex)
            
        print()
            
        declareResultModule.declareResult(playersBlackJack, playersCards, dealersBlackJack, dealersCards, PlayersBet)
        break
    else:
        print('Not Enough cash balance to play')