import os
import copy
import math
from PIL import Image
from Tkinter import DoubleVar
from __init__ import *

EXPORT_PROGRESS = None

CARD_WIDTH = 375
CARD_HEIGHT = 523

W8_5X11 = 1285
H8_5X11 = 1663
MW8_5X11 = 80
MH8_5X11 = 46

class Pack():
    def __init__(self):
        self.cards = []

    def addCard(self, card=None):
        if(isinstance(card, Card)):
            self.cards.append(card)
        else: raise Exception("Card was not passed properly!")

    def addCards(self, cards=None):
        if(isinstance(cards, list)):
            for card in cards: self.addCard(card)
        else: raise Exception("Cards were not passed properly!")

class PackGenerator():
    def __init__(self):
        self.cardPools = {
            RARITY_COMMON: [],
            RARITY_UNCOMMON: [],
            RARITY_RARE: [],
            RARITY_MYTHIC: [],
            TYPE_TOKEN: [],
            TYPE_BASICLAND: []
        }

    def addCardPool(self, cardPool=None):
        if(isinstance(cardPool, CardPool)):
            if(cardPool.type in [TYPE_BASICLAND, TYPE_TOKEN]): self.cardPools[cardPool.type].append(cardPool)
            else: self.cardPools[cardPool.rarity].append(cardPool)
        else:
            raise Exception("CardPool was not passed properly!")

    def generatePack(self, commons=10, uncommons=3, raresMythics=1, lands=1, tokens=1, probabilityMythic=0.33, probabilityFoil=0):
        pack = Pack()

        foils = 0
        foil = random.uniform(0, 1)
        if(foil < probabilityFoil):
            commons -= 1
            foils = 1

        pack.addCards(getCardsFromPools(number=commons, cardPools=self.cardPools[RARITY_COMMON]))
        pack.addCards(getCardsFromPools(number=uncommons, cardPools=self.cardPools[RARITY_UNCOMMON]))

        for counter in range(0, raresMythics):
            mythic = random.uniform(0, 1)
            if(mythic < probabilityMythic): pack.addCards(getCardsFromPools(number=1, cardPools=self.cardPools[RARITY_MYTHIC]))
            else: pack.addCards(getCardsFromPools(number=1, cardPools=self.cardPools[RARITY_RARE]))

        if(foils > 0):
            cards = getCardsFromPools(number=foils, cardPools=self.cardPools[getRandomRarity(probabilityMythic=probabilityMythic)])
            for card in cards:
                foilCard = copy.deepcopy(card)
                foilCard.foil = True
                pack.addCard(foilCard)

        pack.addCards(getCardsFromPools(number=lands, cardPools=self.cardPools[TYPE_BASICLAND]))
        pack.addCards(getCardsFromPools(number=tokens, cardPools=self.cardPools[TYPE_TOKEN]))

        return pack



def printCards(cards=None, output=None, outputPrefix=""):
    if(isinstance(cards, list)):
        if(os.path.isdir(output)):
            frontCanvas = Image.new("RGBA", (W8_5X11, H8_5X11), "#FFFFFF")  # Sheet background
            backCanvas = Image.new("RGBA", (W8_5X11, H8_5X11), "#FFFFFF")  # Card back background
            i = 0
            x = 0
            y = 0

            for card in cards:
                front = Image.open(card.frontFile).resize((CARD_WIDTH, CARD_HEIGHT), Image.ANTIALIAS)
                back = Image.open(card.backFile).resize((CARD_WIDTH, CARD_HEIGHT), Image.ANTIALIAS)

                frontCanvas.paste(front, (MW8_5X11 + CARD_WIDTH * x, MH8_5X11 + CARD_HEIGHT * y))  # Add card to sheet
                backCanvas.paste(back, (MW8_5X11 + CARD_WIDTH * (2 - x), MH8_5X11 + CARD_HEIGHT * y))  # Add back to sheet

                # Move to next card position
                x += 1
                if x >= 3:
                    x = 0
                    y += 1

                    if y >= 3:
                        y = 0
                        # If we've reached the end of the sheet, save it and create a new sheet
                        frontCanvas.save(os.path.join(output, outputPrefix + str(i) + "_front.png"), dpi=(151.182, 151.182))
                        backCanvas.save(os.path.join(output, outputPrefix + str(i) + "_back.png"), dpi=(151.182, 151.182))
                        frontCanvas = Image.new("RGBA", (W8_5X11, H8_5X11), "#FFFFFF")
                        backCanvas = Image.new("RGBA", (W8_5X11, H8_5X11), "#FFFFFF")
                        i += 1

            # Save sheet if there are cards on it
            if not (x == 0 and y == 0):
                frontCanvas.save(os.path.join(output, outputPrefix + str(i) + "_front.png"), dpi=(151.182, 151.182))
                backCanvas.save(os.path.join(output, outputPrefix + str(i) + "_back.png"), dpi=(151.182, 151.182))
        else: raise Exception("Output directory not found!")
    else: raise Exception("Cards were not passed properly!")

def printPacks(packs=None, output=None, savePaper=False):
    global EXPORT_PROGRESS

    if(isinstance(packs, list)):
        cards = []
        counter = 0
        for pack in packs:
            counter += 1
            if(isinstance(pack, Pack)):
                if(not savePaper): printCards(cards=pack.cards, output=output, outputPrefix="pack_"+str(counter)+"_")
                else: cards.extend(pack.cards)
            else: raise Exception("Packs were not passed properly!")
        if(len(cards) > 0): printCards(cards=cards, output=output)
        EXPORT_PROGRESS.set(100)
    else: raise Exception("Packs were not passed properly!")