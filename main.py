# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:00:24 2020

@author: Unmesh
"""

import playersEngine as engineModule
import declareResult as declareResultModule
    
popIndex= 51
playersBlackJack =[]

(dealersBlackJack, popIndex) = engineModule.dealersEngine('Dealer',popIndex)
print()
(playersBlackJack, popIndex) = engineModule.playersEngine('Player',popIndex)


(playersBlackJack, popIndex, playersCards) = engineModule.playersEngineGamblingTime(playersBlackJack,popIndex)
(dealersBlackJack, popIndex, dealersCards) = engineModule.dealersGamblingTime(dealersBlackJack,popIndex)

print()

declareResultModule.declareResult(playersBlackJack, playersCards, dealersBlackJack, dealersCards)
