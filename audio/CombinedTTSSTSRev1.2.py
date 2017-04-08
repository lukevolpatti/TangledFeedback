#The following script reads from a single text file containing all of the questions contained in the Tangled Arts Gallery survey.  Please enter the name of the file under the variable filenameRaw and save this file in the same directory as this python script.
#Install goslate using the following command: pip install goslate
from gtts import gTTS
import os
import playsound

#Change the file name depending on the name of the textfile where the questions are stored.
filenameRaw = "TangledSingleQuestions"
filename = filenameRaw + ".txt"
i = 0
#from tkinter import *
#root = Tk()
import time
import string
import speech_recognition as sr
import goslate
from pygame import mixer

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
        time.sleep(10)
        
        #Playing the French language file
        print(Fr_contents +"\n")
        mixer.init()
        mixer.music.load(audioFr)
        mixer.music.play()
        time.sleep(5)
        
        print("Microphone on")
        aud = r.listen(source)
        print("Done")

    #Acccount for potential error in try statement
    try:
        lang = r.recognize_google(aud)
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
        err1 = gTTS(text = "Il y a eu une erreur.", lang = 'fr')
        audioErr = "err1.mp3"
        err1.save(audioErr)
        mixer.init()
        mixer.music.load(audioErr)
        print("Il y a eu une erreur")
        mixer.music.play()
        time.sleep(5)
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #if there is an error need to return to top without an increment
        err = gTTS(text = "Could not request results from Google Speech Recognition service", lang = 'en')
        audioErr = "err.mp3"
        err.save(audioErr)
        mixer.init()
        mixer.music.load(audioErr)
        mixer.music.play()
        time.sleep(5)
        err2 = gTTS(text = "Il y a eu une erreur.", lang = 'fr')
        audioErr = "err2.mp3"
        err2.save(audioErr)
        mixer.init()
        mixer.music.load(audioErr)
        print("Il y a eu une erreur")
        mixer.music.play()
        time.sleep(5)
        continue
    #marks the answer to question for collection purposes
    t = ','   
    #if i == 0:
    #    t = ''
    
if lang == "we" or lang == "wee" or lang == "We" or lang == "Wee" or lang == "Wheat" or lang == "wheat":
    tutFile = "Tutorial.txt"
    fileTut = open(tutFile, 'r')
    tut_contents = fileTut.read()
    tut_contentsFr = goslate.Goslate().translate(tut_contents, 'fr')
    ttsTutFr = gTTS(text= tut_contentsFr, lang='fr')
    audio = "tutFr.mp3"
    ttsTutFr.save(audio)
    
    #Playing and preparing the tutorial file

    print(tut_contents)
    mixer.init()
    file = open(filename, 'r')
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
        linesFR = goslate.Goslate().translate(lines, 'fr')
        tts = gTTS(text= linesFr, lang='fr')
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
            r = sr.Recognizer('fr')
            with sr.Microphone() as source:
                
                mixer.init()
                mixer.music.load('ansnowFr.mp3')
                print('Répondez')
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
                print("Il y a eu une erreur")
                audioErr = "err2.mp3"
                mixer.init()
                mixer.music.load(audioErr)
                mixer.music.play()
                time.sleep(5)
                #if there is an error need to return to top without an increment
                continue
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                print("Il y a eu une erreur")
                audioErr = "err2.mp3"
                mixer.init()
                mixer.music.load(audioErr)
                mixer.music.play()
                time.sleep(5)
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

#If the selected language is not French, but default it is English
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
