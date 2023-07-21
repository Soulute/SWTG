import os
import random

RARITY_COMMON = "COMMON"
RARITY_UNCOMMON = "UNCOMMON"
RARITY_RARE = "RARE"
RARITY_MYTHIC = "MYTHIC"

TYPE_NORMAL = "NORMAL"
TYPE_BASICLAND = "BASICLAND"
TYPE_TOKEN = "TOKEN"

class Card():
    def __init__(self, frontFile=None, backFile=None, rarity=RARITY_COMMON, type=TYPE_NORMAL):
        frontExtant = False
        if(frontFile != None): frontExtant = os.path.isfile(frontFile)
        backExtant = False
        if(backFile != None): backExtant = os.path.isfile(backFile)

        if(frontExtant and backExtant):
            self.frontFile = frontFile
            self.backFile = backFile
            self.name = os.path.splitext(os.path.basename(self.frontFile))[0]
            self.rarity = rarity
            self.type = type
            self.foil = False
        else:
            msg = ""
            if(not frontExtant and not backExtant): msg = "Image file (front) and image file (back) not found!"
            elif(not frontExtant): msg = "Image file (front) not found!"
            elif(not backExtant): msg = "Image file (back) not found!"

            raise Exception(msg)

    def __str__(self):
        foilStr = ""
        if(self.foil): foilStr = " [FOIL]"
        return self.name + " [" + self.type + "] " + "[" + self.rarity + "]" + foilStr

class CardPool():
    def __init__(self, frontsPath=None, backsPath=None, rarity=RARITY_COMMON, type=TYPE_NORMAL):
        frontsExtant = False
        if(frontsPath != None): frontsExtant = os.path.isdir(frontsPath)
        backsExtant = False
        if(backsPath == None and frontsExtant): backsPath = os.path.join(os.path.dirname(frontsPath), "_backs")
        if(backsPath != None): backsExtant = os.path.isdir(backsPath)

        if(frontsExtant and backsExtant):
            self.frontsPath = frontsPath
            self.backsPath = backsPath
            self.rarity = rarity
            self.type = type
            self.setCards()
        else:
            msg = ""
            if (not frontsExtant and not backsExtant): msg = "Directory (fronts) and directory (backs) not found!"
            elif (not frontsExtant): msg = "Directory (fronts) not found!"
            elif (not backsExtant): msg = "Directory (backs) not found!"

            raise Exception(msg)

    def setCards(self):
        self.cards = []

        backs = {}
        for back in os.listdir(self.backsPath):
            backs[os.path.splitext(back)[0]] = back

        for front in os.listdir(self.frontsPath):
            back = "back.png"
            if os.path.splitext(front)[0] in backs: back = backs[os.path.splitext(front)[0]]

            self.cards.append(Card(os.path.join(self.frontsPath, front), os.path.join(self.backsPath, back), self.rarity, self.type))

    def getCards(self, number=0):
        return pickCards(number=number, pool=self.cards)



def pickCards(number=0, pool=None):
    if(isinstance(pool, list)):
        cards = []
        if(number == 0): return cards
        if(len(pool) == 0): return cards
        tempPool = pool[:]
        for counter in range(0, number):
            if (len(tempPool) == 0): tempPool = pool[:]
            cardNR = random.randint(0, len(tempPool) - 1)
            cards.append(tempPool[cardNR])
            tempPool.remove(tempPool[cardNR])
        return cards
    else: raise Exception("Pool were not passed properly!")

def getCardsFromPools(number=0, cardPools=None):
    if(isinstance(cardPools, list)):
        tempPool = []
        for cardPool in cardPools:
            if(isinstance(cardPool, CardPool)):
                tempPool.extend(cardPool.cards)
            else: raise Exception("CardPools were not passed properly!")
        return pickCards(number=number, pool=tempPool)
    else: raise Exception("CardPools were not passed properly!")

def getRandomRarity(probabilityMythic=0):
    rand = random.uniform(0, 14)
    if rand <= 10: return RARITY_COMMON
    elif rand <= 13: return RARITY_UNCOMMON
    elif rand <= 14 - probabilityMythic: return RARITY_RARE
    else: return RARITY_MYTHIC