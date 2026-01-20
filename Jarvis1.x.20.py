import datetime
import os
import random
import smtplib
import sys
import pyjokes
import webbrowser
import pywhatkit
import psutil
import pyttsx3
import pywikihow
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha
from bs4 import BeautifulSoup

try:
    app = wolframalpha.Client("4H6WTL-K3QLPEWAT4")
except Exception:
    print('error')

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    currentH = int(datetime.datetime.now().hour)

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am  Jarvis!')
speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        speak('user: ' +query+ '\n')

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()


        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        
        elif 'open whatsapp' in query:
            speak('okay')
            webbrowser.open('web.whatsapp.com')
        
        elif 'play my favourite song' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=JJnUiv61fFg')

        elif 'my brother has gone for a minute' in query:
            speak('okay')
            speak('hello my iron man fan')
            speak('hahah')

        elif 'can you play some song'in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=AW3-SuBZRt0')
        
        elif 'search' in query:
            results = wikipedia.summary(query, sentences=2)
            speak('Got it.')
            speak('WIKIPEDIA says - ')
            speak(results)


        elif 'thakur edusprint'in query:
            speak('okay sir opening')
            webbrowser.open('https://thakur.edusprint.in/thakur')

        elif 'calendar' in query:
            speak('opening calender')
            open('https://calendar.google.com/calendar')


        elif 'datetime' in query:
            now = datetime.datetime.now()
            speak(datetime)

        elif 'play my second favourite song' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=LBr7kECsjcQ')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')


        elif 'open my school account' in query:
            speak('okay sir opening you school')
            webbrowser.open('https://mail.google.com/mail/u/1/#inbox')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

        elif 'it thinks that i have slept for just five minutes' in query:
            speak('yes sir i know')

            if 'Nutan' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('nutanshety83@gmail.com',)
                    server.ehlo()
                    server.starttls()
                    server.login("nutanshety83@gmail.com", 'Ganesh2112*')
                    server.sendmail('nutanshety83@gmail.com', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


            else:
                temp=query.replace(' ','+0')
                g_url=("https://www.google.com/search?q=")
                res_g='sorry pls search on your own'
                print(res_g)
                speak(res_g)



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hey how are you?' in query:
            speak('im doing ok sir')

        elif 'open notepad'in query:
            speak('okay')
            os.startfile('C:\\windows\\system32\\notepad.exe')


        elif 'word'in query:
            speak('okay sir open os.file')
            os.startfile('C:\\program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')

        elif 'my cool song' in query:
            speak('ok sir playing your personlized music')
            webbrowser.open('https://www.youtube.com/watch?v=WCTjFHyvEaM')


        elif 'how much battery is there my laptop'in query:
            speak('okay sir')
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")

       
           

        elif 'temperature'in query:
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp} ")
    
        elif 'time' in query:
            speak('okay')
            time = datetime.datetime.now().strftime('%I:%M:%S')
            speak(time)

        elif 'date' in query:
            speak('okay')
            date = datetime.datetime.now().strfdatetime('%Y-%m-%d')
            speak(date)

        elif 'show my location' in query:
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            city = data['city']
            speak(city)



        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')

            sys.exit()

        elif 'good afternoon jarvis' in query:
            speak('good afternoon sir')
            


        elif "google search"in query:
            speak('what should i search in google?')
            cm= myCommand().lower()
            webbrowser.open(f"{cm}")


        elif 'activate how to do a mod' in query:
            #from pywikihow import search_wikihow
            speak('how to do a mod is now activated')
            how = myCommand()
            max_results = 1
            how_to = pywikihow.search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif 'i want to play a game' in query:
            speak('ok sir')
            speak('starting your game')
            os.startfile('C:\\Users\\mrpar\\OneDrive\\Python projects\\gamejarvis.py')

        elif 'whatsapp message to my papa'in query:
            speak('ok sir what should i say and to whom')
            speak('number identified pls tell the message')
            message = myCommand()
            pywhatkit.sendwhatmsg('+91 9867302857', message,22,22)
            webbrowser.open('https://pypi.org/project/pywhatkit/')


        elif 'play some song'in query:
            speak('which song you want to play sir?')
            song = myCommand()
            speak('intialization in process')
            speak('playing' +song)
            webbrowser.open('https://www.youtube.com/results?search_query+{song}')

        elif 'whatsapp message to mahi' in query:
            speak('ok sir what should i say and to whom')
            speak('number identified pls tell the message')
            message = myCommand()
            speak(message) 
            pywhatkit.sendwhatmsg('+91 77100 08221', message, 14,14)

        elif 'calculations'in query:
            speak('what to do sir?')
            plus = myCommand()
            subtract = myCommand()
            multiply = myCommand()
            divide = myCommand()
            if 'plus'in query():
                speak('pls tell the number')
                number1 = myCommand()
                speak('number2')
                number2 = myCommand()
                plus = number1+number2
                speak(plus)

        elif 'my schedule'in query:
            speak('ok sir')
            webbrowser.open('https://calendar.google.com/calendar/u/1/r/day/2021/9/6?tab=mc&pli=1')
            speak(webbrowser)
        
        elif'activate weight identifier'in query:
            #activate
            speak('activating')
            speak('which planet')
            Planet=myCommand()
            if 'moon'in Planet:
                weightonEarthcurrent=float(input("Enter you current weight on Earth: "))
                weightonmoon=round((weightonEarthcurrent*1.622)/9.81,2)
                speak("weight on moon is " + str(weightonmoon))

        elif'activate friday'in query:
            speak('calling my sister')
            os.startfile('C:\Users\mrpar\OneDrive\Python projects\Friday.py')


        
            






                
                

    

        

            
            

        


 
