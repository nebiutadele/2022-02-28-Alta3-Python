#!/usr/bin/python3

# Create a black jack hand

# Import random utility
import random


# Variables of card
values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = ['H', 'C', 'D', 'S']

# Deck creation
cards = []

for suit in suits:
    for value in values:
        cards.append((suit, value))

# All cards created
print(cards)
# Shuffle deck
random.shuffle(cards)
print(cards)
print("\n\n")
#Remove two cards
print(cards.pop())
print(cards.pop())
