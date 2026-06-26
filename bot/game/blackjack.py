"""
Blackjack game logic
"""

import random
import logging
from enum import Enum
from typing import List, Tuple

logger = logging.getLogger(__name__)

class CardSuit(Enum):
    """Card suits"""
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

class CardRank(Enum):
    """Card ranks"""
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

class Card:
    """Represents a playing card"""
    
    def __init__(self, rank: CardRank, suit: CardSuit):
        self.rank = rank
        self.suit = suit
    
    def get_value(self) -> int:
        """Get the value of the card"""
        if self.rank.value in ['J', 'Q', 'K']:
            return 10
        elif self.rank.value == 'A':
            return 11
        else:
            return int(self.rank.value)
    
    def __str__(self):
        return f"{self.rank.value}{self.suit.value}"

class Deck:
    """Represents a deck of cards"""
    
    def __init__(self, num_decks: int = 1):
        self.cards: List[Card] = []
        self.num_decks = num_decks
        self.reset()
    
    def reset(self):
        """Reset the deck"""
        self.cards = []
        for _ in range(self.num_decks):
            for suit in CardSuit:
                for rank in CardRank:
                    self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)
    
    def draw(self) -> Card:
        """Draw a card from the deck"""
        if len(self.cards) < 10:
            self.reset()
        return self.cards.pop()

class Hand:
    """Represents a hand of cards"""
    
    def __init__(self):
        self.cards: List[Card] = []
    
    def add_card(self, card: Card):
        """Add a card to the hand"""
        self.cards.append(card)
    
    def get_value(self) -> int:
        """Get the value of the hand"""
        value = 0
        aces = 0
        
        for card in self.cards:
            if card.rank == CardRank.ACE:
                aces += 1
                value += 11
            else:
                value += card.get_value()
        
        # Adjust for aces
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value
    
    def is_blackjack(self) -> bool:
        """Check if hand is blackjack"""
        return len(self.cards) == 2 and self.get_value() == 21
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

class BlackjackGame:
    """Main Blackjack game class"""
    
    def __init__(self, wallet_manager):
        self.wallet_manager = wallet_manager
        self.deck = Deck()
        self.player_hand = None
        self.dealer_hand = None
    
    def start_game(self) -> Tuple[Hand, Hand]:
        """Start a new game"""
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        # Deal cards
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        
        return self.player_hand, self.dealer_hand
    
    def hit(self, hand: Hand) -> Card:
        """Hit (draw a card)"""
        card = self.deck.draw()
        hand.add_card(card)
        return card
    
    def stand(self) -> int:
        """Stand and calculate result"""
        # Dealer hits until 17
        while self.dealer_hand.get_value() < 17:
            self.hit(self.dealer_hand)
        
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        
        if player_value > 21:
            return -1  # Player bust
        elif dealer_value > 21:
            return 1   # Dealer bust
        elif player_value > dealer_value:
            return 1   # Player wins
        elif player_value < dealer_value:
            return -1  # Dealer wins
        else:
            return 0   # Draw
