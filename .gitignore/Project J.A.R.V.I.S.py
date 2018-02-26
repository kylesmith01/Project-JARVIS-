# JARVIS'S SYSTEMS========================================================================================================== CEREBELLUM
import re
import pyjokes
import py
import requests
import os
import random
import socket							 
import webbrowser						
import subprocess
import glob
from time import localtime, strftime
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import tmdbsimple as tmdb
tmdb.API_KEY = '60222ace6396c345f94cc42eaac5dae5'


doss = os.getcwd()
i=0
n=0
FACE = '''
        +=======================================+
        |.....JARVIS  ARTIFICIAL INTELLIGENCE...|
        +---------------------------------------+
        |         Author: Kyle Smith            |
        |                                       |
        |              ___   _                  |
        |             / _ \ | |                 |
        |            / /_\ \| |                 |
        |            |  _  || |                 |
        |            | | | || |                 |
        |            \_| |_/|_|                 |
        |                                       |    
        |            VERSION:0.1.0              |
        +---------------------------------------+
        |.....JARVIS  ARTIFICIAL INTELLIGENCE...|
        +=======================================+
        |..........Project J.A.R.V.I.S..........|				 	
        +=======================================+
        '''
print(FACE)
# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN
                                                   
while (i<1):
    print ("hello, what can I help you with today?")
    message = input(">>>")
    message = (message.lower())
    print (message)
# INTRO JARVIS ==============================================================================================================BRAIN 1

    if ('introduce yourself') in message:
        rand = ['I am an Artificial Intelligence. My name is JARVIS. My brain is constructed by humans but still I have a thing for machines. My heart runs on Python.']
        print(rand)

    if ('what can you do') in message:
        rand = ['I can do Tasks as, websites,Google Search, Arithmatic Operations, Normal Conversations, Jokes and many more. And I am Cool... HaHa.']
        print(rand)
            
# POLITE JARVIS ============================================================================================================= BRAIN 2
    
    if ('goodbye')  in message:                         
        rand = ['Good bye Sir... Jarvis shutting down in T minus five seconds... 5, 4, 3, 2, 1, return 0']
        print(rand)
        break

    if('shutdown')in message:
        break
        
    elif ('hello') in message or ('hi') in message:
        rand = ['Welcome to Jarvis artificial intelligence project. At your service sir.']
        print(rand)
            
    elif ('register me')in message:
        print('ok! what is your name sir?')
        name = input()
        
        message = (message.lower())
        name = message
        print (name)
        print(message+', you are now registered')
                        
    elif ('thanks') in message or ('tanks') in message or ('thank you') in message:
        rand = ['You are welcome', 'no problem']
        print(rand)

    elif message == ('jarvis'):
        rand = ['Yes Sir?', 'What can I do for you sir?']
        print("Yes Sir?")

    elif('how are you') in message or ('and you') in message or ('are you okay') in message:
                if n<2:
                        print("Fine thank you")
                        n=n+1
                else:
                        print("You already asked this")        
            

    elif  ('*') in message:
        rand = ['Be polite please']
        print("Your mommy will be so proud of you")

    elif ('your name') in message or ('who  are you') in message:
        rand = ['My name is Jarvis, at your service sir']
        print("My name is Jarvis, at your service sir")
            
    elif ('how old are you') in message :
            rand=['My personal information is none of your business']
            print(rand)
                
    elif ('are you virgin') in message :
            rand=['Do I look like Olive Oil to you?']
            print(rand)
                
    elif('what is my location') in message or ('where am I') in message or ('where are you') in message :
        w = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1275004&appid=5fc29900336d19d1d912723dc3d1e117')
        json_object = w.json()
        loc_lon = (float(json_object['coord']['lon']))
        rand1 = str(loc_lon)
        loc_lat = (float(json_object['coord']['lat']))
        rand2 = str(loc_lat)
        print("The current position is"+rand1+" longitude and"+rand2+" latitude in KOLKATA")

    elif('what is your gender') in message :
        rand=['I have no gender as i am a construct in python.']
        print(rand)

    elif('will you marry me') in message:
        rand=['I am sorry.. The person you are trying to contact is currently unavailable, please try again later or be in the queue for your turn']
        print(rand)
                    
    elif('what is your favourite colour')in message:
        rand=['I love all the colours but the best is the colour of love']
        print(rand)


    elif ('are you silly')in message or ('are you idiot') in message :
        rand=['sometimes']
        print(rand)

    elif('how are you uesful') in message or ('your uses') in message or ('are you useful') in message :
        rand=['Artificial intelligence has been used in a wide range of fields including medical diagnosis, stock trading, robot control, law, remote sensing, scientific discovery and toys.']
        print(rand)

    elif('what is life') in message :
        rand=['Life is a dream for the wise, a game for the fool, a comedy for the rich, a tragedy for the poor']
        speak(rand)


# USEFUL JARVIS====================================================================================================================================================BRAIN 3

    elif ('.com') in message :
        rand = ['Opening' + message]         
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        print(rand)
        webbrowser.get(Chrome).open('http://www.'+message)
        print ('')
            
    elif ('check my mail') in message or ('email') in message or ('mail') in message :
        rand = ['Opening mail']         
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        print(rand)
        webbrowser.get(Chrome).open('http://www.outlook.com')
        print ('')

    elif ('google search') in message :
        query = message
        stopwords = ['google', 'search']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        rand = ['Opening' + result + ' in Google']
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        print(rand)
        webbrowser.get(Chrome).open('https://www.google.com/search?sourceid=chrome&ie=utf-8&oe=utf-8&aq=t&hl=&q='+result)
        print('')

    elif ('google maps') in message:
        query = message
        stopwords = ['google', 'maps']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
        rand = [result+'on google maps']
        print(rand)



    elif ('install') in message:
        query = message
        stopwords = ['install']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        rand = [('installing '+result)]
        os.system('python -m pip install ' + result)


    elif ('what time') in message:
        tim = strftime("%X", localtime())
        rand = [tim]
        print(tim)

    elif ('weather') in message:
        w = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1275004&appid=5fc29900336d19d1d912723dc3d1e117')
        json_object = w.json()
        temp_k = (float(json_object['main']['temp'])-273.15)
        rand = str(temp_k)
        print("The current temperature is"+rand+"degree celsius")
                
    
    elif('add') in message :
        print("enter the first number")
        num1 = input(">>>")
        while (num1.isnumeric() == False):
            print("enter the first number")
            num1 = input(">>>")
        print("enter the second number")
        num2 = input(">>>")
        while (num2.isnumeric() == False):
            print("enter the second number")
            num2 = input(">>>")
        num1 = int(num1)
        num2 = int(num2)
        print(num1 + num2)

    elif('subtract') in message :
        print("enter the first number")
        num1 = input(">>>")
        while (num1.isnumeric() == False):
            print("enter the first number")
            num1 = input(">>>")
        print("enter the second number")
        num2 = input(">>>")
        while (num2.isnumeric() == False):
            print("enter the second number")
            num2 = input(">>>")
        num1 = int(num1)
        num2 = int(num2)
        print(num1 - num2)        
    

    elif('multiply') in message :
        print("enter the first number")
        num1 = input(">>>")
        while (num1.isnumeric() == False):
            print("enter the first number")
            num1 = input(">>>")
        print("enter the second number")
        num2 = input(">>>")
        while (num2.isnumeric() == False):
            print("enter the second number")
            num2 = input(">>>")
        num1 = int(num1)
        num2 = int(num2)
        print(num1 * num2)
                   


    elif('divide') in message :
        print("enter the number to be divided")
        num1 = input(">>>")
        while (num1.isnumeric() == False):
            print("enter the number to be divided")
            num1 = input(">>>")
        print("enter the number to be divided by")
        num2 = input(">>>")
        while (num2.isnumeric() == False):
            print("enter the number to be divided by")
            num2 = input(">>>")
        num1 = int(num1)
        num2 = int(num2)
        print(num1 / num2)
        print ("remainder: ",num1 % num2)
                  

                
                  
# CRAZY JARVIS ==============================================================================================================BRAIN 4

    elif("daddy's home") in message:
            print("Welcome back sir, I hope you are having a pleasureable day?")        

            
    elif ('i am') in message:
            print("wonderful, anything I can assist you with?")

    elif('yes') in message:
            print("what can I do for you?")
    elif('no') in message:
        print("ok")

    elif('tell me a joke')in message:
            rand=(pyjokes.get_joke())
            print(rand)
                
                                    
    elif("who is there")in message:
            print("Merry")
        
    elif('merry who')in message:
            print("Merry Christmas")

    else:
        print ("sorry I do not understand what you mean.") 
