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
#from tkinter import *
#root = Tk()
import time
import string
import speech_recognition as sr
from pygame import mixer
tutFile = "Tutorial.txt"
fileTut = open(tutFile, 'r')
tut_contents = fileTut.read()
tts2 = gTTS(text= tut_contents, lang='en')
audio = "tut.mp3"
tts2.save(audio)
fName = path + "\\" + filename
file = open(filename, 'r')
f_contents = file.read()
mixer.init()
mixer.music.load(audio)
mixer.music.play()
time.sleep(21)
stringArr = f_contents.split("\n")
#print(stringArr)

text_file = open("CSVAnswers.csv","a")
text_file.write("\n")
text_file.close()
tts1 = gTTS(text = 'Please answer now', lang='en')
tts1.save("ansnow.mp3")
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
    time.sleep(8)
    j=0
    while j < 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            mixer.init()
            mixer.music.load('ansnow.mp3')
            print('ansnow')
            mixer.music.play()
            time.sleep(2)
            print("Question here:")
            aud = r.listen(source)
            print('Done')
    
        #Acccount for potential error in try statement
        try:
            print("Your Answer here: " + r.recognize_google(aud))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            #if there is an error need to return to top without an increment
            continue
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            #if there is an error need to return to top without an increment
            continue
        #marks the answer to question for collection purposes
        t = ','   
        #if i == 0:
        #    t = ''
        
            
                
        #could add bit that reads out your asnwer to the question here
        #write the text into a document for data collection
        text_file = open("CSVAnswers.csv","a")
        text_file.write(t + r.recognize_google(aud))
        text_file.close()
        j += 1      #increment counter