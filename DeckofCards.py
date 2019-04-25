import random

class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

class Deck(object):
    def __init__(self):
        cardlist = ["hearts", "diamonds", "clubs", "spades"]
        self.cards = []
        for x in cardlist:
            for y in range(1,14):
                newcard = Card(x,y)
                self.cards.append(newcard)
        
    def shuffle(self):
        for i in range(0, len(self.cards)):
           rand = random.randint(0, 51)
           temp = self.cards[i]
           self.cards[i] = self.cards[rand]
           self.cards[rand]=temp       
        return self

    def deal(self):
        card=self.cards.pop()
        return card

class Monkey(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
    def draw(self,deck):
        card = deck.deal()
        self.hand.append(card)
        return self 
player1 = Monkey("bob")
print player1.name

newdeck = Deck()
for i in newdeck.cards:
    print i.value, i.suit

newdeck.shuffle()
for i in newdeck.cards:
    print i.value, i.suit

player1.draw(newdeck)
print "first hand", player1.hand[0].value, player1.hand[0].suit
