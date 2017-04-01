#The following script reads from a single text file containing all of the questions contained in the Tangled Arts Gallery survey.  Please enter the path where the text file is stored under the variable path and the name of the file under the variable filenameRaw
from gtts import gTTS
import os
import playsound
#Change the path depending on where you store the audio files
path = "C:\\Users\\josh123\\Documents\\ESC102\\TangledQuestions2"
#Change the file name depending on the name of the textfile where the questions are stored.
filenameRaw = "TangledSingleQuestions"
filename = filenameRaw + ".txt"
i = 0
from tkinter import *
root = Tk()
import time
import string

from pygame import mixer
fName = path + "\\" + filename
file = open(fName, 'r')
f_contents = file.read()
stringArr = f_contents.split("\n")
#print(stringArr)
for lines in stringArr:
    
    print(lines)
    # fileVar = open(fName, "r")
    # file_contents = fileVar.read()
    # print(file_contents)
    i = str(i)
    tts = gTTS(text= lines, lang='en')
    audio = "good" + i + ".mp3"
    tts.save(audio)
    i = int(i)
    i = i + 1
    
    
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()
    time.sleep(15)
    

