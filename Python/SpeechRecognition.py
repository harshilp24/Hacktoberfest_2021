import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import pdb
import test
import math
import requests
from currency_converter import CurrencyConverter
from datetime import date
from tabulate import tabulate

#engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
client = wolframalpha.Client('AJ9E83-X9V6EQKGGH')

voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[len(voices) - 1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    if currentH >= 12 and currentH < 16:
        speak('Good Afternoon!')
    if currentH >= 16 and currentH != 0:
        speak('Good Evening!')

greetMe()
speak('Hello, I am your lady assistant "Sophie..."')
speak('How may I help you?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say")
        print ('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        query = r.recognize_google(audio)
        print ('User: ' + query + '\n')	

    except sr.UnknownValueError:
        speak('Sorry! I didn\'t get that. Try typing the command!')
        query = str(input('Command: '))

    return query

def sendEmail(to, subject, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(test.EMAIL_ADDRESS, test.PASSWORD)
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail(test.EMAIL_ADDRESS, to, message)
    server.quit()

if __name__ == '__main__':

    while True:
        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'send an email' in query:
            speak('Who is the recipient?')
            recipient = str(input('Recipient: '))

            if 'me' in recipient or 'myself' in recipient:
                try:
                    to = test.EMAIL_ADDRESS
                    speak('What should be the subject of the mail ?')
                    subject = str(input('Subject: '))
                    speak('What should be the body of the mail ?')
                    msg = str(input('Subject: '))
                    sendEmail(to, subject, msg)
                    speak("Hurray...Email sent")
                except:
                    speak('Oops...Email not sent')
            else:
                try:
                    to = recipient
                    speak('What should be the subject of the mail ?')
                    subject = str(input('Subject: '))
                    speak('What should be the body of the mail ?')
                    msg = str(input('Subject: '))
                    sendEmail(to, subject, msg)
                    speak("Hurray...Email sent")
                except:
                    speak('Oops...Email not sent')

        elif 'nothing' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Bye, have a good day.')
            break;

        elif 'hello' in query or 'hey' in query:
            speak('Hello')

        elif 'current time' in query or 'time today' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'currency' in query or 'currency conversion' in query:
            speak("Sure. I can help you with that. Here is the list of currency conversions I offer:")
            print(tabulate([['US-Dollar', 'USD'], ['Indian-Rupee', 'INR'],['Euro', 'EUR'],['Pound-Sterling', 'GBP'],['Australian-Dollar', 'AUD'],['Canadian-Dollar', 'CAD'],['Swiss-Franc','CHF'],['Swedish-Krona','SEK'],['New-Zealand-Dollar','NZD']], headers=['Curreny Name', 'Currency Code']))
            print("")
            speak("Please tell the currency code you wish to convert from")
            currencyFrom = myCommand()
            speak("Please tell the currency code you wish to convert to")
            currencyTo = myCommand()
            speak("Please tell the amount you wish to convert")
            currencyAmount = myCommand()
            c = CurrencyConverter(fallback_on_wrong_date=True)
            dateValue = datetime.datetime.now()
            currency_value = c.convert(currencyAmount, currencyFrom.upper(), currencyTo.upper(), date=date(dateValue.year, dateValue.month, dateValue.day))
            #rounded_currency_value = (round(currency_value, 3))
            speak(f"The converted currency value is {currency_value}")

        elif 'temperature' in query or 'weather' in query:
            speak("Please tell me your city")
            city = myCommand()
            api_address="http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            url = api_address + city
            json_data = requests.get(url).json()
            weather_desc = json_data['weather'][0]['description']
            temp_kelvin = json_data['main']['temp']
            temp_cels = temp_kelvin - 273.15
            temp_cels_ceil_value = math.ceil(temp_cels)
            speak(f"The current temperature in {city} is { temp_cels_ceil_value} degrees")

        elif 'music' in query or 'songs' in query or 'song' in query:
            music_dir = 'C:\\Users\\i322214\\Desktop\\songs\\'
            songs = os.listdir(music_dir)
            secure_random = random.SystemRandom()
            os.startfile(music_dir + secure_random.choice(songs))

        else:
            query = query
            speak('Searching..')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('As per my information - ')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=3)
                    speak('WIKIPEDIA says - ')
                    speak(results)
            except:
                speak("Let me search this on google for you...")
                webbrowser.open('www.google.com/search?q='+ query)
        speak('Next Command! Please...')
