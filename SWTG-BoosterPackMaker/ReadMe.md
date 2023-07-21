#**GITHUB NOTICE**

1. /dist/dist.zip needs to be unpacked to function
   
2. To save on space, only example card images remain in the resources directory. To get the complete resources, go to https://www.starwarsthegathering.com/play.html
   
#**END GITHUB NOTICE**


SWTG-PackGenerator



A booster pack generator for Star Wars: The Gathering.
https://www.starwarsthegathering.com/



--------
Starting the program
--------


**Windows**


This folder contains the "SWTG-PackGenerator.bat" file for Windows. You can run it by double-clicking. It is possible that your anti-virus program deletes the batch file for security reasons. This is normal as batch files can be malicious. In this case it is NOT!

However, if there is no "SWTG-PackGenerator.bat" file just go into the "dist" folder and run the "createPack.exe".



**Linux** (tested under Debian 8)


You need to install the following packages:


apt-get install python-tk python-imaging


In the "python" directory are the python source files. If you have python installed, you should be able to run the program over the command line by "python createPack.py".





--------
How to use
--------


If you have succesfully started the program, a GUI should appear in which you can make your settings for the booster packs.



**Options**


*Commons:* Number of commons in the packs


*Uncommons:* Number of uncommons in the packs


*Rares / Mythic:* Number of rares / mythics in the packs


*Lands:* Number of lands in the packs


*Tokens:* Number of tokens in the packs


*Mythics P. (%):* Chance of getting a mythics instead of rares


*Foils P. (%):* Chance of getting a foil card


*Number of Packs:* Number of packs you want to create




*new pages for each pack:* Creates each pack on different sites. Makes it easier to draft, but wastes some paper.

 (recommended)
*save paper:* Creates all cards of each pack consecutively without empty space on the sites.





**Actions**


*GENERATE:* Generates the packs and lists them in the box on the left when ready.


*EXPORT:* Exports the packs to image files for printing. You are asked to choose an export directory in which the files will be stored. When the export is done, the progress bar under this button will be fully filled.


*You can navigate through the generated packs by the "<" and ">" buttons or by scrolling inside the box.


--------
How to upload different cards
--------


If you want to use a different set or to update to newer versions of the set, here's how the folders are set up:

There is a folder for each of commons, uncommons, rares, mythics, tokens and lands inside the "resources" directory. Just put the cards in their respective folders.

The cards have to be 375x523 pixels. 

If you have a double-sided card, put the front side in the folder as normal, but put the back side (which should line up and be the same size) in the back folder. 

It must have the same name as the file for the front side. The pack generator will look for any files in the back folder with the same name and if it finds one it will use that for the back, otherwise it will use the "back.png" file.





--------
Misc
--------
For the SWTG community, visit *

https://www.reddit.com/r/swtg


Comments or questions? Message /u/SoulofZendikar via Reddit anytime.

v1 by /u/MimeJabsIntern

v2 (GUI update) by /u/Superperforat0r

Maintained by /u/SoulofZendikar
