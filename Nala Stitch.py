import random
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
    
    def __str__(self):
        return f"{self.color}({self.value})"

#==================================================================================================
#COMPARE CARDS
#==================================================================================================

def compare(playerCard, pileCard):
    compatible = False
    #print(playerCard)
    if (playerCard.getValue() == pileCard.getValue()):
        compatible = True
    elif (playerCard.getColor() == pileCard.getColor()):
        compatible = True
    #elif (playerCard.getValue() > 12):
        #compatible = True
    else:
        compatible = False
    return compatible
    
#==================================================================================================
#COMPARE HAND TO PILE
#==================================================================================================

def checkHand(playerHand, pileCard):
    r = False
    for card in playerHand:
        #print(card)
        match = compare(card, pileCard)
        if(match == True):
            print('Hand Match')
            r = True
        else:
            print('No Hand Match')
    return r

def generate_Card():
        colors_list = ['Red', 'Blue', 'Green', 'Yellow']
        color = random.choice(colors_list)
        random_num = random.randrange(1, 10) #I eliminated wild cards 
        #number = 4
        #temp_color = "Red"
        card = Card(color, random_num)
        return card

def turn(player_hand, pileCard, whichPlayer):#possibly import whose turn it is
    turnOver = False
    print('Player', whichPlayer)
    print('Your Hand')
    [print(i, end = ' ') for i in player_hand]
    print('\n The pile card is', pileCard)
    if checkHand(player_hand, pileCard) == True:
        while turnOver == False:
            chosenIndex = int(input('choose card to put down by index:'))
            chosen = player_hand[chosenIndex]
            print('you chose', chosen)
            if compare(chosen, pileCard) == True:
                nextPileCard = chosen
                player_hand.pop(chosenIndex)
                turnOver = True
                print('turn done')
                return nextPileCard
            else:
                print('compare denied')
                #print("card chosen doesn't match the pile")
                turnOver = False
    else:
        #print('before add', player_hand)
        player_hand.append(generate_Card()) #player must take card and does not get a chance to put them down
        print('You have been forced to draw a card and it has been added to your hand')
        #print('after add', player_hand)
        return pileCard

#At some point turn function is run and returns the nextPileCard
def main():
    numPlayers = int(input("How many players are there? "))
    allHands = []
    for player in range(numPlayers):
        player_hand = []
        for card in range(7): 
            card = generate_Card()
            player_hand.append(card)
        print('Player', player,':')
        [print(i, end = ' ') for i in player_hand]
        print('\n')
        allHands.append(player_hand)
    deckCard1 = generate_Card()
    nextPileCard = 0
    nextPileCard1 = 0
    #nextPileCard2 = 0
    """
    whichPlayer = 1
    for player in allHands:
        nextPileCard = turn(player_hand, deckCard1, whichPlayer)
        whichPlayer += 1
    """
    nextPileCard = deckCard1
    while(len(player_hand) > 0):
        whichPlayer = 1
        for player in allHands:
            nextPileCard1 = turn(player_hand, nextPileCard, whichPlayer)
            whichPlayer += 1
            nextPileCard = nextPileCard1
    print("A player has gotten rid of all their cards and they have won. Game Over!!")

#if __name__ == '__main__':
main()