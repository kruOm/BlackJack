# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:47:25 2020

@author: Unmesh
"""


import generateDeck as generateDeck
import BlackJack as blackjack
    
popIndex= 51  

deck = generateDeck.generateDeck()
generateDeck.shuffleDeck(deck)

def playersEngine(playerOrDealer,deck, popIndex):
    playersCards = []
    playerCard1 = generateDeck.pickCard(deck,popIndex)
    popIndex = popIndex-1
    playerCard2 = generateDeck.pickCard(deck,popIndex)
    popIndex = popIndex-1
    playersCards.append(playerCard1)

    playersCards.append(playerCard2)

    print(playerOrDealer,'has:')
    generateDeck.printCard(playerCard1)
    generateDeck.printCard(playerCard2)
    playersBlackJackValue = playerCard1.value + playerCard2.value
    playersBlackJack = blackjack.blackjack('Player', playersBlackJackValue,playersCards)
    return(playersBlackJack,popIndex, deck)    

def playersEngineGamblingTime(playersBlackJack,deck,popIndex):
    playersBlackJackValue = playersBlackJack[1]
    playersCards = playersBlackJack[3]
    
    while (input('Hit Me (Y/N) ? ') == 'Y'):
        playerCard3 = generateDeck.pickCard(deck, popIndex)
        popIndex = popIndex-1
        
        generateDeck.printCard(playerCard3)
        
        
        
        playersCards = playersBlackJack[3]
        playersCards.append(playerCard3)
        
        
        playersBlackJackValue += playerCard3.value
        playersBlackJack = blackjack.blackjack('Player', playersBlackJackValue,playersCards)
        if playersBlackJack[2]=='Bust':
            break
        
    return(playersBlackJack,popIndex, playersCards, deck)

def dealersEngine(playerOrDealer,deck ,popIndex):
    
    dealersCards = []
    dealerCard1 = generateDeck.pickCard(deck,popIndex)
    popIndex = popIndex-1
    dealerCard2 = generateDeck.pickCard(deck,popIndex)
    popIndex = popIndex-1
    dealersCards.append(dealerCard1)
    dealersCards.append(dealerCard2)

    print(playerOrDealer,'has:')
    generateDeck.printCard(dealerCard1)
    print('*Hidden*')
    dealersBlackJackValue = dealerCard1.value + dealerCard2.value
    
    
    dealersBlackJack = blackjack.blackjack('Dealer', dealersBlackJackValue,dealersCards)

    return(dealersBlackJack,popIndex, deck)

def dealersGamblingTime(dealersBlackJack,deck,popIndex):
    dealersBlackJackValue = dealersBlackJack[1]
    dealersCards = dealersBlackJack[3]

    while (dealersBlackJackValue<=15):
        
        dealerCard3 = generateDeck.pickCard(deck, popIndex)
        popIndex = popIndex-1
        dealersCards.append(dealerCard3)
        
        
        
 
        dealersBlackJackValue += dealerCard3.value
        dealersBlackJack = blackjack.blackjack('Dealer', dealersBlackJackValue,dealersCards)
        if dealersBlackJack[2]=='Bust':
            break

    return(dealersBlackJack,popIndex,dealersCards,deck)
