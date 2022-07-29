# XP-Startup-Sound
 Plays an earrape version of the windows startup sound, on startup.
 
**Works for Windows so far, not tested on Mac/Linux**

### Build / Setup Instructions:

1. Download source code and extract to anywhere on your computer.
2. Configure INFO.txt
- Line1 : Volume (0-100)
- Line2 : Sound file (name.type)
3. Open main.pyw so you can edit it. (In notepad, python IDLE, VSC, etc)
4. Change line 5, and set it to the path of the extracted folder.
5. In command prompt:
- pip3 install pynput
- pip3 install playsound
- pip3 install pyinstaller
6. Then, open command prompt in the folder. (Either open git bash or navigate to the folder via the command 'cd *folder*'
7. Run **pyinstaller --onefile main.pyw**
8. The .exe file can be found in /dist/main/
9. Copy main.exe
10. Press *Windows Key*+R
11. Type 'shell:startup', and press enter.
12. Paste main.exe into that folder.
13. Done!

### Notes
**Each time you change something, you will need to re-build the .exe file (Steps 6-13)**
If you want to change the sound, just add the sound file into the folder. Then, in the INFO.txt file, change line 2 to the name of the sound file.
To change the volume, change line 1 of INFO.txt


