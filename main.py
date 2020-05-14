# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:00:24 2020

@author: Unmesh
"""

class PlayersCash():
    
    def __init__(self,cashBalance):
        self.cashBalance = cashBalance
        
    def bet(self,bet):
        self.bet = bet
    
    def updateBalance(self,winnings):
        self.cashBalance = self.cashBalance + winnings
        print('You bet: $', self.bet, ' You won: $', winnings, ' Your balance is: $', self.cashBalance)


def playAgain(deck,popIndex):

    print('PopIndex is ',popIndex)
    PlayersBet.bet = int(input('Place your bets please ? $'))    
        
    (dealersBlackJack, popIndex, deck) = engineModule.dealersEngine('Dealer',deck, popIndex)


    (playersBlackJack, popIndex, deck) = engineModule.playersEngine('Player',deck, popIndex)
    
    
    
    
    (playersBlackJack, popIndex, playersCards, deck) = engineModule.playersEngineGamblingTime(playersBlackJack,deck,popIndex)
    (dealersBlackJack, popIndex, dealersCards, deck ) = engineModule.dealersGamblingTime(dealersBlackJack,deck,popIndex)
        
    print()
        
    declareResultModule.declareResult(playersBlackJack, playersCards, dealersBlackJack, dealersCards, PlayersBet)

    
import playersEngine as engineModule
import declareResult as declareResultModule
import generateDeck as generateDeckModule      
popIndex= 51
playersBlackJack =[]
gameplay =0    

suit = ['Heart','Spades','Clubs','Diamonds']
rank = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
deck = []
        
inputcash = input('How much $ would you like to begin with ?')
inputcash = int(inputcash)
PlayersBet = PlayersCash(inputcash)

deck = generateDeckModule.generateDeck(suit,rank,deck)
generateDeckModule.shuffleDeck(deck)

if gameplay == 0:
    playAgain(deck,popIndex)

    while (input('Do you want to play again ?')=='Y'):
        deck = generateDeckModule.generateDeck(suit,rank,deck)
        generateDeckModule.shuffleDeck(deck)
        playAgain(deck,popIndex)
    else:
        print('Thank you for playing. We hope you enjoyed it here. Your total Cash Balance is $',PlayersBet.cashBalance)







