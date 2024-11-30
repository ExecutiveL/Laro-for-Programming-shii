import pygame
from pygame import mixer
import random

pygame.init()

SUITS = ['H', 'D', 'S', 'C']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def get_font(size):
 return pygame.font.Font("asset/Grand9KPixel.ttf", size)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
    
    #Building the deck
    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))
        
    #using random to shuffle the cards
    def shuffle(self):
        random.shuffle(self.cards)
        
    #dealing a card from the deck
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
        
            
class Laro:
    def __init__(self):
        self.deck = Deck()
        self.current_card = None
        self.next_card = None
        self.money = 500
        
        
    def start_game(self):
        self.current_card = self.deck.deal()
        self.next_card = self.deck.deal()
    
    def round_start(self, guess):
        # Tinitignan kung available ang cards
        if self.current_card is None or self.next_card is None:
            return False

        # kinukuha ang current and next card rank
        Current_rank = RANKS.index(self.current_card[0])
        next_rank = RANKS.index(self.next_card[0])

        # Checking kung tama ang guess ng user
        if (guess == "Higher" and next_rank > Current_rank) or (guess == "Lower" and next_rank < Current_rank):
            self.money += 0
            result = True
        else:
            result = False

        # Update cards
        self.current_card = self.next_card
        self.next_card = self.deck.deal()

        return result

    
    def get_current_card(self):
        return self.current_card
    #kinukuha ang score after ng laro
    def get_money(self):
        return self.money
    #niloload ang image based current_card
   
    #niloload ang image based current_card
    def load_card_image(self,card):
     if card is None:
        return None
     return pygame.image.load(f"asset/{card[0]}{card[1]}.png")
 