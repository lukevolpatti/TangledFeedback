from gtts import gTTS
import os
import playsound
#Change the path depending on where you store the audio files
path = "C:\\Users\\josh123\\Documents\\ESC102\TangledQuestions"
i = 0
from tkinter import *
root = Tk()
import time
    
from pygame import mixer
for filename in os.listdir(path):
    fName = path + "\\" + filename
    file = open(fName, 'r')
    f_contents = file.read()
    print(f_contents)
    # fileVar = open(fName, "r")
    # file_contents = fileVar.read()
    # print(file_contents)
    i = str(i)
    tts = gTTS(text= f_contents, lang='en')
    audio = "good" + i + ".mp3"
    tts.save(audio)
    i = int(i)
    i = i + 1
    
    
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()
    time.sleep(15)
    
    #root.mainloop()
    # #root.quit()
    # 
    # 
    # root.mainloop()
    # #root.quit()
    # #root.destroy()
