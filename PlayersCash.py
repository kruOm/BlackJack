# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:22:24 2020

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