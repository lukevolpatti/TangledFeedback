#The following script reads from a single text file containing all of the questions contained in the Tangled Arts Gallery survey.  Please enter the name of the file under the variable filenameRaw and save this file in the same directory as this python script.
#Please do not overuse French option: Daily limit of 1,000,000 characters and 10,000,000 characters per month

#Making sure modules have been installed
import pip

def install(package):
    pip.main(['install', package])
    
install('gtts')
install('playsound')
install('SpeechRecognition')
install('pygame')
install('yandex.translate')

#Importing necessary modules
from gtts import gTTS
import os
import playsound
import winsound
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
from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20170411T042600Z.53c6be29aceef06b.4f83f7c8cae230ab9b1f197476f48c1dd2f34433')
#Creating English Error message

tts5 = gTTS(text = "An error has occurred.", lang = 'en')
audioErrEn = "ErrEn.mp3"
tts5.save(audioErrEn)

#Creating French Error message
tts6 = gTTS(text = "Il y a eu une erreur.", lang = 'fr')
audioErrFr = "ErrFr.mp3"
tts6.save(audioErrFr)

def enError():
        mixer.init()
        mixer.music.load(audioErrEn)
        print("An error has occurred.")
        mixer.music.play()
        time.sleep(3)
        
def frError():
        mixer.init()
        mixer.music.load(audioErrFr)
        print("Il y a eu une erreur.")
        mixer.music.play()
        time.sleep(3)

#Reading the English language selection file

langEnFile = "LanguageSelectionEnglish.txt"
fileEn = open(langEnFile, 'r')
En_contents = fileEn.read()
tts3 = gTTS(text = En_contents, lang = 'en')
audioEn = "en.mp3"
tts3.save(audioEn)

#Reading the French language selection file

langFrFile = "LanguageSelectionFrench.txt"
fileFr = open(langFrFile, 'r')
Fr_contents = fileFr.read()
tts4 = gTTS(text = Fr_contents, lang = 'fr')
audioFr = "fr.mp3"
tts4.save(audioFr)
j=0
#Respondent chooses language
while j < 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        mixer.init()
        #Playing the English language file
        print(En_contents)
        mixer.init()
        mixer.music.load(audioEn)
        mixer.music.play()
        time.sleep(15)
        
        #Playing the French language file
        print(Fr_contents +"\n")
        mixer.init()
        mixer.music.load(audioFr)
        mixer.music.play()
        time.sleep(5)
        
        print("Microphone on")
        winsound.Beep(440, 250) # frequency, duration
        time.sleep(0.25)        # in seconds (0.25 is 250ms)
        aud = r.listen(source)
        print("Done")

    #Acccount for potential error in try statement
    try:
        lang = r.recognize_google(aud, key = None, language = "en-US", show_all = False)
        #lang = r.recognize_google(aud)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        #if there is an error need to return to top without an increment
        err = gTTS(text = "Google Speech Recognition could not understand audio", lang = 'en')
        audioErr = "err.mp3"
        err.save(audioErr)
        mixer.init()
        mixer.music.load(audioErr)
        mixer.music.play()
        time.sleep(5)
        enError()
        frError()
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #if there is an error need to return to top without an increment
        err66 = gTTS(text = "Could not request results from Google Speech Recognition service", lang = 'en')
        audioErr = "err66.mp3"
        err.save(audioErr)
        mixer.init()
        mixer.music.load(audioErr)
        mixer.music.play()
        time.sleep(5)
        enError()
        frError()
        continue
    #marks the answer to question for collection purposes
    t = ','   
    #if i == 0:
    #    t = ''
    j = j + 1
    
if lang == "we" or lang == "wee" or lang == "We" or lang == "Wee" or lang == "Wheat" or lang == "wheat":
    tutFile = "TutorialFr.txt"
    fileTut = open(tutFile, 'r')
    tut_contents = fileTut.read()
    ttsTutFr = gTTS(text= tut_contents, lang='fr')
    audio = "tutFr.mp3"
    ttsTutFr.save(audio)
    
    #Playing and preparing the tutorial file

    print(tut_contents)
    mixer.init()
    file = open(filenameRaw + "Fr" + ".txt", 'r')
    f_contents = file.read()
    mixer.music.load(audio)
    mixer.music.play()
    time.sleep(26)
    
    #Respondent answering questions
    
    stringArr = f_contents.split("\n")
    #print(stringArr)
    
    text_file = open("CSVAnswers.csv","a")
    text_file.write("\n")
    text_file.close()
    ttsFrAns = gTTS(text = 'Veuillez répondre maintenant', lang='fr')
    ttsFrAns.save("ansnowFr.mp3")
    for lines in stringArr:
        
        print(lines)
        # fileVar = open(fName, "r")
        # file_contents = fileVar.read()
        # print(file_contents)
        i = str(i)
        tts = gTTS(text= lines, lang='fr')
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
                mixer.music.load('ansnowFr.mp3')
                print('Répondez')
                mixer.music.play()
                time.sleep(2)
                print("Question here:")
                aud = r.listen(source)
                winsound.Beep(440, 250) # frequency, duration
                time.sleep(0.25)        # in seconds (0.25 is 250ms)
                print('Done')
        
            #Acccount for potential error in try statement
            try:
                print("Your Answer here: " + r.recognize_google(aud, language = 'fr'))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                frError()
                #if there is an error need to return to top without an increment
                continue
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                frError()
                #if there is an error need to return to top without an increment
                continue
            #marks the answer to question for collection purposes
            t = ','   
            #if i == 0:
            #    t = ''
            
                
                    
            #could add bit that reads out your asnwer to the question here
            #write the text into a document for data collection
            text_file = open("CSVAnswers.csv","a")
            transtext = r.recognize_google(aud, language = 'fr')
            #Using Yandex API to translate
            a = translate.translate(transtext, 'en')
            text = a['text']
            text_Fr = text[0]
            text_file.write(t + text_Fr)
            text_file.close()
            j += 1      #increment counter    

#If the selected language is not French, by default it is English
else:
    #Reading the tutorial file
    tutFile = "Tutorial.txt"
    fileTut = open(tutFile, 'r')
    tut_contents = fileTut.read()
    tts2 = gTTS(text= tut_contents, lang='en')
    audio = "tut.mp3"
    tts2.save(audio)
    
    #Playing and preparing the tutorial file
    file = open(filename, 'r')
    f_contents = file.read()
    print(tut_contents)
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()
    time.sleep(21)
    #Respondent answering questions
    
    
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
                winsound.Beep(440, 250) # frequency, duration
                time.sleep(0.25)        # in seconds (0.25 is 250ms)
                print('Done')
        
            #Acccount for potential error in try statement
            try:
                print("Your Answer here: " + r.recognize_google(aud))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                enError()
                #if there is an error need to return to top without an increment
                continue
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                #if there is an error need to return to top without an increment
                enError()
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