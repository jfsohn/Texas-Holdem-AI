#Indiana Reed (ijreed) & Jake Sohn (jfsohn)
#CSCI-B351
#Final Project - Texas Holdem AI

from itertools import groupby
from operator import itemgetter

hand = [None] * 2
board = [None] * 5


hand = [0,5]
board = [13,14,15,16,18]
cards = sorted(hand+board)

#takes a list of cards
#finds pairs, 3 of a kind, 4 of a kind
def findPairs(cards):
    pairs = set() #set of tuples in the form (number of duplicates, card)
    card = 0
    for card1 in cards:
        temp = 0
        for card2 in cards:
            if card2%13 == card1%13:
                temp += 1
        if temp >= 2:
            card = card1%13
            pairs.add((temp, card))
    if len(pairs) != 0:
        return pairs
    else:
        return None

#takes a list of cards
#finds flush
def findFlush(cards):
    clubs = []
    diamonds = []
    hearts = []
    spades = []
    #add all cards to respective suits
    for card in cards:
        if card in range(0,12):
            clubs.append(card)
        elif card in range(13,25):
            diamonds.append(card)
        elif card in range(26, 38):
            hearts.append(card)
        else:
            spades.append(card)
    #if any suit has 5 cards, return the cards
    #(sort and take the 5 highest cards)
    if len(clubs) >= 5:
        return sorted(clubs)[-5:]
    elif len(diamonds) >= 5:
        return sorted(diamonds)[-5:]
    elif len(hearts) >= 5:
        return sorted(hearts)[-5:]
    elif len(spades) >= 5:
        return sorted(spades)[-5:]
    else:
        return None

#takes a list of cards
#finds straight
##def findStraight(cards):
##    for k,g in groupby(enumerate(cards), lambda (i, x): i-x):
##        print (map(itemgetter(1), g))

print(findPairs(cards))
print(findFlush(cards))
#print(findStraight(cards))
