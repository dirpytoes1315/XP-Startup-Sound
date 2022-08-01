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
6. Using [https://gist.github.com/dirpytoes1315/91dea15d2413ddcde497b5933d0d11e0](This Tutorial), create the main.exe file. The folder name is what you set the name of the folder to (Usually XP-Startup-Sound), and the file name is *main.pyw*
7. Copy main.exe
8. Press *Windows Key*+R
9. Type 'shell:startup', and press enter.
10. Paste main.exe into that folder.
11. Done!

### Notes
**Each time you change something, you will need to re-build the .exe file (Steps 6-13)**
If you want to change the sound, just add the sound file into the folder. Then, in the INFO.txt file, change line 2 to the name of the sound file.
To change the volume, change line 1 of INFO.txt


