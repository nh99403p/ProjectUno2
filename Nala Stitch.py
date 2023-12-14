import random
#def check_hand(player_card, pile_card):
plus = 1

#==================================================================================================
#CARD CODE
#==================================================================================================

class Card:

    def __init__ (self, init_color, init_value):
        self.color = init_color
        self.value = init_value
    
    def setColor (self, param):
        self.color = param
    
    def setValue (self, param):
        self.value = param

    def getColor (self):
        return self.color
    
    def getValue (self):
        return self.value
    
    def toString (self):
        color = self.color
        value = self.value
        if self.value < 10:
            name = color + " " + str(value)
        elif value == 10:
            name = color + " Skip"
        elif value == 11:
            name = color + " +2"
        elif value == 13:
            name = "Wild Card"
        elif value == 14:
            name = "+4 Card"
        else:
            name = "Something went wrong..."
        
#==================================================================================================
#COMPARE CARDS
#==================================================================================================

def compare(playerCard, pileCard):
    compatible = False
    print("compare", playerCard.getValue())
    print("compare", pileCard.getValue())
    print("compare", playerCard.getColor())
    print("compare", pileCard.getColor())
    print(playerCard.toString())
    if (playerCard.getValue() == pileCard.getValue()):
        print(playerCard.getValue())
        print(pileCard.getValue())
        compatible = True
    elif (playerCard.getColor() == pileCard.getColor()):
        compatible = True
    elif (playerCard.getValue() > 12):
        compatible = True
    else:
        compatible = False
    #if (playerCard.getValue() > 9):
        #checkSpecial(playerCard)
    return compatible
    
#==================================================================================================
#COMPARE HAND TO PILE
#==================================================================================================

#player hand is list of tuples
def checkHand(playerHand, pileCard):
    for card in playerHand:
        #print(card)
        match = compare(card, pileCard)
        if(match == True):
            print('Hand Match')
            return True
        else:
            print('No Hand Match')
            return False

#def main():

    #hand = [Card("Red", 5), ("Green", 'red'), (3, 'blue')]
    #hand1 = [Card("Special", 13)]
    #checkHand(hand1, Card("Red", 1))
    #return
#Testers    
#compare((3, 'red'), (3, 'red'))

#def checkSpecial(card):
    #if(card[0] == 10):
        #skip_tracker +=2
    #if(card[0] == 11):
        #plus = 2
    #if(card[0] == 12):
        #wild()
    #if(card[0] == 13):
        #plus = 4
        #wild()

def generate_Card():
        colors_list = ['Red', 'Blue', 'Green', 'Yellow', 'Special']
        color = random.choice(colors_list)
        random_num = random.randrange(1, 10) #I eliminated wild cards 
        number = 4
        temp_color = "Red"
        card = Card(temp_color, number)
        return card
"""
def main():
    #numPlayers = int(input("How many players are there? "))
    numPlayers = 2
    for player in range(numPlayers):
        player_hand = []
        for player in range(7): 
            #card = Generate_Card()
            #card = ('Red', 2)
            card = ('Red', 2) #Prints something weird when I try to print card class
            player_hand.append(card)
        print(player_hand)
    deckCard1 = Generate_Card()
    while(player_hand.length > 1):

    return
"""


def turn(player_hand, pileCard):
    turnOver = False
    print('Your Hand')
    for card in player_hand:
        print(card.toString)
    #print('Your Hand','\n',player_hand)
    if checkHand(player_hand, pileCard) == True:
        while turnOver == False:
            chosenIndex = int(input('choose card to put down by index:'))
            chosen = player_hand[chosenIndex]
            print(chosen)
            if compare(chosen, pileCard) == True:
                nextPileCard = chosen
                turnOver = True
                print('turn done')
                return nextPileCard
            else:
                print('compare denied')
                #print("card chosen doesn't match the pile")
                turnOver = False
    else:
        print('before add', player_hand)
        player_hand.append(generate_Card()) #player must take card and does not get a chance to put them down
        print('You have been forced to draw a card and it has been added to your hand')
        print('after add', player_hand)
        return player_hand

def main():   
    #fake_hand = [Card('Red', 2), Card('Red', 2), Card('Red', 2), Card('Red', 2), Card('Red', 2), Card('Red', 2), Card('Red', 2)]
    fake_hand = [Card('Red', 2), Card('Blue', 3)]
    fake_card = Card('Red', 2)
    turn(fake_hand, fake_card)
    return

#How are the cards in the hand labeled, and what does the player type in to select a card
if __name__ == '__main__':
    main()