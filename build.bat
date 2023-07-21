RMDIR /S /Q "./dist"
python "python/setup.py" py2exe
RMDIR /S /Q "./build"

ECHO cd dist > "SWTG-PackGenerator.bat"
ECHO createPack.exe >> "SWTG-PackGenerator.bat"