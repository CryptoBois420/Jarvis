import speech_recognition as sr
import pyttsx3
import os
import wolframalpha
import datetime
import asyncio
import python_weather
import webbrowser
import sys
import os
import cv2
import mediapipe as mp
import time

# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
while(1):

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        SpeakText("Good Morning!")
        SpeakText("I am Jarvis Sir. Please tell me how may I help you")
    elif hour>=12 and hour<18:
        SpeakText("Good Afternoon!")
        SpeakText("I am Jarvis Sir. Please tell me how may I help you")   
    else:
        SpeakText("Good Evening!")  
        SpeakText("I am Jarvis Sir. Please tell me how may I help you") 
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            SpeakText("Sir i am listening")
            print("I am listening")
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText == "stop":
                sys.exit()

            if MyText == "hand tracking":
            #figure out how to make python open a file with os or something

            if MyText == "open youtube":
                webbrowser.open("youtube.com")

            if MyText == "open facebook":
                webbrowser.open("facebook.com")
                
            if MyText == "open discord":
                webbrowser.open("discord.gg")                          

            if MyText == "what is the time":
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                SpeakText(f"Sir, the time is {strTime}")

            if MyText == "i have a question":
                # Taking input from user
                question = input('Question: ')
 

# App id obtained by the above steps
                app_id = "XPGH56-6LUPH896V9"
  
# Instance of wolf ram alpha 
# client class
                client = wolframalpha.Client(app_id)
  
# Stores the response from 
# wolf ram alpha
                res = client.query(question)
  
# Includes only text from the response
                answer = next(res.results).text
  
                print(answer)
                SpeakText('sir the answer is ' + answer)

        continue
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
