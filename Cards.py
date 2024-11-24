import pygame
from pygame import mixer
import random

pygame.init()

SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9']
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)



def get_font(size):
 return pygame.font.Font("asset/Grand9KPixel.ttf", size)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
     
    #nilalagay sa self.card na list
    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))
        print(self.cards)
    #shinuffle ang list by using the rarndomn
    def shuffle(self):
        random.shuffle(self.cards)
        
    #IF yung shinuffle na card ay asa dulo ng list ippop nya
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()
            
class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0 
  
    def add_card(self, card):
        self.cards.append(card)
    #ADDING THE VALUES
    def calc_hand(self):
        first_card_index = [a_card[0] for a_card in self.cards]
        non_aces = [c for c in first_card_index if c != 'A']
        aces = [c for c in first_card_index if c == 'A']

        for card in non_aces:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)

        for card in aces:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1


    def display_cards(self):
        for card in self.cards:
            cards = "".join((card[0], card[1]))
            if cards not in self.card_img:
                self.card_img.append(cards)
    
