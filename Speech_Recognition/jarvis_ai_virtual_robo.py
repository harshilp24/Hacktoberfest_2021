import pyttsx3
import datetime # work with current system date time packages.
import speech_recognition as sr # speach to text library  # pip install SpeechRecognition
import wikipedia # To Search From Wikipedia website.
import smtplib # To send mail to other users
import webbrowser as wb #  searching from websites

# from utils import *

engine = pyttsx3.init()  # object creation
engine.setProperty('rate', 210)     # setting up new voice rate
# changing index, changes voices. 1 for female
engine.setProperty('voice', engine.getProperty('voices')[1].id)



def speak(audio):
    """
    Function for Speaking from computer
    """ 
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def time():
    """    
    Show the system current date and time and Speak 
    """
    
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():
    """
    Shows the system date and speak.    
    """
    
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    # print(year, month, date)
    speak("The current date is ")
    speak(year)
    speak(month)
    speak(date)


def wishhing():
    """
     First Wishing.
    """
    
    speak("Welcome sir,")
    time()
    speak("jarvis at your service, how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 5
        audio = r.listen(source)
        print("audio", audio)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say again please...")
        return "None"
    except KeyboardInterrupt as e:
        print("Forcefully exit")

    return query


def sendMail(to, content,):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echo()
    server.starttls()
    server.login('your_email_address', 'your_email_password')
    server.sendmail('sendedr_email_address', to, content)
    server.close()


if __name__ == "__main__":
    wishhing()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia", '')
            result = wikipedia.summary(query, sentence=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what to say?")
                content = takeCommand()
                to = 'vikas.ukani@dignizant.com'
                sendMail(to, content)
                speak("Email sent")
            except Exception as e:
                print(e)
                speak("unable to send email!")

        elif 'search' in query:
            speak("what to search")
            # web_path = ""
            wb.open('http://google.com/' + query)

        elif 'offline' in query:
            quit()
