# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:00:24 2020

@author: Unmesh
"""



import generateDeck as generateDeckModule
import PlayersCash as PlayersCashClass
import playAgain as playAgainModule

popIndex= 51
playersBlackJack =[]
gameplay =0    

deck = []
        
inputcash = input('How much $ would you like to begin with ?')
inputcash = int(inputcash)
PlayersBet = PlayersCashClass.PlayersCash(inputcash)

deck = generateDeckModule.generateDeck()
generateDeckModule.shuffleDeck(deck)

if gameplay == 0:
    playAgainModule.playAgain(PlayersBet, deck,popIndex)

    while (input('Do you want to play again ?')=='Y'):
        deck = generateDeckModule.generateDeck()
        generateDeckModule.shuffleDeck(deck)
        playAgainModule.playAgain(PlayersBet, deck,popIndex)
    else:
        print('Thank you for playing. We hope you enjoyed it here. Your total Cash Balance is $',PlayersBet.cashBalance)







