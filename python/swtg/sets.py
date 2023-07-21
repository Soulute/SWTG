import os
from __init__ import *

class Set():
    def __init__(self, path=None):
        pathExtant = False
        if (pathExtant != None): pathExtant = os.path.isdir(path)

        if(pathExtant):
            self.path = path
            pathSplit = os.path.split(path)
            self.name = pathSplit[len(pathSplit) - 1]
            self.setCardPools()
        else: raise Exception("Path not found!")

    def setCardPools(self):
        self.cardPools = []

        for directory in os.listdir(self.path):
            directoryPath = os.path.join(self.path, directory)
            if(os.path.isdir(directoryPath)):
                if(directory == "commons"): self.cardPools.append(CardPool(frontsPath=directoryPath, rarity=RARITY_COMMON))
                elif(directory == "uncommons"): self.cardPools.append(CardPool(frontsPath=directoryPath, rarity=RARITY_UNCOMMON))
                elif(directory == "rares"): self.cardPools.append(CardPool(frontsPath=directoryPath, rarity=RARITY_RARE))
                elif(directory == "mythics"): self.cardPools.append(CardPool(frontsPath=directoryPath, rarity=RARITY_MYTHIC))
                elif(directory == "basiclands"): self.cardPools.append(CardPool(frontsPath=directoryPath, type=TYPE_BASICLAND))
                elif(directory == "tokens"): self.cardPools.append(CardPool(frontsPath=directoryPath, type=TYPE_TOKEN))