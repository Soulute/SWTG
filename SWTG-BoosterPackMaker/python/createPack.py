import platform
import tkFileDialog
from Tkinter import *
from ttk import Progressbar
from swtg import *

def previousPack():
    global PACK_SELECTED

    PACK_SELECTED -= 1
    if(PACK_SELECTED < 0): PACK_SELECTED = 0
    listBoxPacks.see(PACK_SELECTED * 18 +8)

def nextPack():
    global PACK_SELECTED

    PACK_SELECTED += 1
    if (PACK_SELECTED > len(PACKS)): PACK_SELECTED = len(PACKS) - 1
    listBoxPacks.see(PACK_SELECTED * 18 + 8)

def exportPacks():
    output = tkFileDialog.askdirectory(parent=window,initialdir="/",title='Please select a directory')
    if(output != ""):
        packs.EXPORT_PROGRESS.set(0)
        progressBar.update()
        printPacks(packs=PACKS, output=output, savePaper=SAVE_PAPER.get())

def generatePacks():
    global PACKS

    generator = PackGenerator()

    for set in SETS:
        if(set["active"].get()):
            for cardPool in set["set"].cardPools:
                generator.addCardPool(cardPool=cardPool)

    PACKS = []
    for counter in range(0, int(entryPacksNumber.get())):
        pack = generator.generatePack(
            commons=int(entryCommonsNumber.get()),
            uncommons=int(entryUncommonsNumber.get()),
            raresMythics=int(entryRaresMythicsNumber.get()),
            lands=int(entryLandsNumber.get()),
            tokens=int(entryTokensNumber.get()),
            probabilityMythic=float(entryMythicsProbability.get()),
            probabilityFoil=float(entryFoilsProbability.get())
        )
        PACKS.append(pack)

    listBoxPacks.delete(0, END)

    counter = 1
    for pack in PACKS:
        listBoxPacks.insert(END, "--- Pack " + str(counter) + " of " + str(len(PACKS)) + " ---")
        for card in pack.cards:
            listBoxPacks.insert(END, str(card))
        listBoxPacks.insert(END, "---")
        counter += 1
    listBoxPacks.pack()

def main():
    window.wm_title("SWTG-PackGenerator")
    if(platform.system() == "Windows"):
        window.iconbitmap("../icon.ico")
    window.minsize(0, 0)
    window.resizable(width=False, height=False)

    frameSets.pack(fill=BOTH, side=LEFT)
    framePacks.pack(fill=BOTH, side=LEFT)
    frameOptions.pack(fill=BOTH, side=LEFT)

    framePacksHeadline.pack(fill=X, side=TOP)
    frameGenerateOptions.pack(fill=X, side=TOP)
    frameExportOptions.pack(fill=X, side=BOTTOM)
    frameOptionsHeadline.pack(fill=X, side=TOP)
    frameCommonsNumber.pack(fill=X, side=TOP)
    frameUncommonsNumber.pack(fill=X, side=TOP)
    frameRaresMythicssNumber.pack(fill=X, side=TOP)
    frameLandsNumber.pack(fill=X, side=TOP)
    frameTokensNumber.pack(fill=X, side=TOP)
    frameMythicsProbability.pack(fill=X, side=TOP)
    frameFoilsProbability.pack(fill=X, side=TOP)
    framePacksNumber.pack(fill=X, side=TOP)
    buttonGenerate.pack(fill=X, side=TOP)
    frameSavePaper.pack(fill=X, side=TOP)
    buttonExport.pack(fill=X, side=TOP)
    frameSetsHeadline.pack(fill=X, side=TOP)
    frameSetsContent.pack(fill=BOTH, side=TOP)

    labelPacks.pack(side=LEFT)
    buttonNext.pack(side=RIGHT)
    buttonPrevious.pack(side=RIGHT)
    labelOptions.pack(fill=X)
    listBoxPacks.pack()

    labelCommonsNumber.pack(side=LEFT)
    entryCommonsNumber.insert(0, "10")
    entryCommonsNumber.pack(side=RIGHT)
    labelUncommonsNumber.pack(side=LEFT)
    entryUncommonsNumber.insert(0, "3")
    entryUncommonsNumber.pack(side=RIGHT)
    labelRaresMythicsNumber.pack(side=LEFT)
    entryRaresMythicsNumber.insert(0, "1")
    entryRaresMythicsNumber.pack(side=RIGHT)
    labelLandsNumber.pack(side=LEFT)
    entryLandsNumber.insert(0, "1")
    entryLandsNumber.pack(side=RIGHT)
    labelTokensNumber.pack(side=LEFT)
    entryTokensNumber.insert(0, "1")
    entryTokensNumber.pack(side=RIGHT)
    labelMythicsProbability.pack(side=LEFT)
    entryMythicsProbability.insert(0, "0.334")
    entryMythicsProbability.pack(side=RIGHT)
    labelFoilsProbability.pack(side=LEFT)
    entryFoilsProbability.insert(0, "0.167")
    entryFoilsProbability.pack(side=RIGHT)
    labelPacksNumber.pack(side=LEFT)
    entryPacksNumber.insert(0, "1")
    entryPacksNumber.pack(side=RIGHT)

    radioButtonSavePaperFalse.pack(fill=X, side=TOP)
    radioButtonSavePaperTrue.pack(fill=X, side=TOP)
    progressBar.pack(fill=X, expand=1)

    labelSets.pack(side=LEFT)

    for directory in os.listdir(RESOURCES_DIR):
        set = Set(path=os.path.join(RESOURCES_DIR, directory))
        SETS.append({"set":set, "active":BooleanVar()})
        SETS[-1]["active"].set(False)
        if(set.name in SETS_SELECTED): SETS[-1]["active"].set(True)
        checkBoxSet = Checkbutton(frameSetsContent, text=set.name, variable=SETS[-1]["active"], anchor=W)
        checkBoxSet.pack(fill=X, side=TOP)

    window.mainloop()

window = Tk()

RESOURCES_DIR = os.path.join("..", "resources")
SETS = []
SETS_SELECTED = ["SWTG - Main"]
PACKS = []
PACK_SELECTED = 0
SAVE_PAPER = BooleanVar()
SAVE_PAPER.set(False)
packs.EXPORT_PROGRESS = DoubleVar()
packs.EXPORT_PROGRESS.set(0)

framePacks = Frame(window)
framePacksHeadline = Frame(framePacks)
frameOptions = Frame(window)
frameGenerateOptions = Frame(window)
frameExportOptions = Frame(window)
frameOptionsHeadline = Frame(frameGenerateOptions)
frameCommonsNumber = Frame(frameGenerateOptions)
frameUncommonsNumber = Frame(frameGenerateOptions)
frameRaresMythicssNumber = Frame(frameGenerateOptions)
frameLandsNumber = Frame(frameGenerateOptions)
frameTokensNumber = Frame(frameGenerateOptions)
frameMythicsProbability = Frame(frameGenerateOptions)
frameFoilsProbability = Frame(frameGenerateOptions)
framePacksNumber = Frame(frameGenerateOptions)
frameSavePaper = Frame(frameExportOptions)
frameSets = Frame(window)
frameSetsHeadline = Frame(frameSets)
frameSetsContent = Frame(frameSets)

labelPacks = Label(framePacksHeadline, text="Packs", anchor=W)
buttonPrevious = Button(framePacksHeadline, text="<", command=previousPack)
buttonNext = Button(framePacksHeadline, text=">", command=nextPack)
labelOptions = Label(frameOptionsHeadline, text="Options", anchor=W)
listBoxPacks = Listbox(framePacks, height=18, width=50)

labelCommonsNumber = Label(frameCommonsNumber, text="Commons:", anchor=W)
entryCommonsNumber = Entry(frameCommonsNumber, width=5)
labelUncommonsNumber = Label(frameUncommonsNumber, text="Uncommons:", anchor=W)
entryUncommonsNumber = Entry(frameUncommonsNumber, width=5)
labelRaresMythicsNumber = Label(frameRaresMythicssNumber, text="Rares / Mythics:", anchor=W)
entryRaresMythicsNumber = Entry(frameRaresMythicssNumber, width=5)
labelLandsNumber = Label(frameLandsNumber, text="Lands:", anchor=W)
entryLandsNumber = Entry(frameLandsNumber, width=5)
labelTokensNumber = Label(frameTokensNumber, text="Tokens:", anchor=W)
entryTokensNumber = Entry(frameTokensNumber, width=5)
labelMythicsProbability = Label(frameMythicsProbability, text="Mythics P. (%):", anchor=W)
entryMythicsProbability = Entry(frameMythicsProbability, width=5)
labelFoilsProbability = Label(frameFoilsProbability, text="Foils P. (%):", anchor=W)
entryFoilsProbability = Entry(frameFoilsProbability, width=5)
labelPacksNumber = Label(framePacksNumber, text="Number of Packs:", anchor=W)
entryPacksNumber = Entry(framePacksNumber, width=5)
buttonGenerate = Button(frameGenerateOptions, text="GENERATE", command=generatePacks)

radioButtonSavePaperFalse = Radiobutton(frameSavePaper, text="new pages for each pack", variable=SAVE_PAPER, value=False, anchor=W)
radioButtonSavePaperTrue = Radiobutton(frameSavePaper, text="save paper", variable=SAVE_PAPER, value=True, anchor=W)
buttonExport = Button(frameExportOptions, text="EXPORT", command=exportPacks)
progressBar = Progressbar(frameExportOptions, orient=HORIZONTAL, variable=packs.EXPORT_PROGRESS)

labelSets = Label(frameSetsHeadline, text="Sets", anchor=W)

if __name__ == "__main__":
    main()