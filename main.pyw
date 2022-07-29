from pynput.keyboard import Key,Controller
import playsound

keyboard = Controller()
PATH = 'C:/Users/Henry/OneDrive/Projects/XP-Startup-Sound/' # ADD YOUR PATH TO STARTUP FOLDER HERE

def main():
    info = []
    with open(PATH + 'INFO.txt') as infoFile:
        while (line := infoFile.readline().rstrip()):
            info.append(line)
    VOLUME = int(int(info[0]) / 2)
    SOUND = info[1]
    print(VOLUME, SOUND)
    
    for i in range(100):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)

    for i in range(VOLUME):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

    playsound.playsound(PATH + SOUND)

if __name__ == "__main__":
    main()
