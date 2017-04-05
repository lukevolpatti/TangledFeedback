#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
i = 0
''' THIS IS THE ORIGINAL COPIED FORMATTING WITH THEIR COMMENTS
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

text_file = open("TangledAnswers.txt","a")
text_file.write("*" + r.recognize_google(audio) + "*\n")
text_file.close()
'''
#iterate through as many times as there is questions
while i < 3:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Question here:")
        audio = r.listen(source)
 
    #Acccount for potential error in try statement
    try:
        print("Your Answer here: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        #if there is an error need to return to top without an increment
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #if there is an error need to return to top without an increment
        continue
    #marks the answer to question for collection purposes
    t = '*'   
    if i == 0:
        t = ''
    
        
            
    #could add bit that reads out your asnwer to the question here
    #write the text into a document for data collection
    text_file = open("TangledAnswers.txt","a")
    text_file.write(t + r.recognize_google(audio))
    text_file.close()
    i += 1      #increment counter
    
    
    
    
 
#need to scan file and pick out line that would represent the answer to each question
#Then take that answer and put into another file with easch value seperated by commas
copy = 0
write_csv = open("CSVAnswers.txt", "a")
h = open("TangledAnswers.txt", "r")
text_doc = h.read()
for j in text_doc:
    
    if  j == '*': 
        write_csv.write(", ")
        continue
    write_csv.write(j)
    
    
h.close()
write_csv.close()