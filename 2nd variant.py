import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0]) #scan select voices by changing index
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning!')
    
    elif hour>12 and hour<18:
        speak('good afternoon!')

    else:
        speak('good evening')

    speak('My name is MEEMAA , how can i help you?')
def takecommand():
    #it takes microphone input from user and takes string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)#to recognise error

        print("say that again please...")
        return "None"
    return query    

def sendEmail(to, content):#not working sorry
    server = smtplib.SMTP('smtp.gmail.com', 578)
    server.ehlo()
    server.starttls()
    server.login('sayant2001@gmail.com', 'Sayanth@02$')
    server.sendmail('sayant2001@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query=takecommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        
        elif ' youtube' in query:
            webbrowser.get('windows-default').open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.get('windows-default').open('http://www.google.com')

        elif 'open whatsapp' in query:
            webbrowser.get('windows-default').open('https://web.whatsapp.com/')

        elif 'search' in query:
            
            query = query.replace('search','')
            url = 'https://google.com/search?q=' + query
            webbrowser.get().open(url)
            speak('Here is what i found for ' + query)

        elif 'youtube' in query:
            
            query = query.replace('youtube','')
            url = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.get().open(url)
            speak('Here is what i found for ' + query)

        elif 'open games' in query:
            os.startfile('E:\\STEAM\\steam')
            speak('opening steam games')

            
        elif 'open teams' in query:
            os.startfile('C:\\Users\\sayan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams')
            speak('opening teams')

        elif 'r6' in query:
            os.startfile('C:\\Users\\sayan\\OneDrive\\Desktop\\GAMES\\RainbowSix')
            speak('opening R6')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\sayan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'send email' in query:#still in devlopment
            try:
                speak("what should i say?")
                content = takecommand()
                to = "sayant2001@gmail.com"
                sendEmail(to, content)
                speak('email has been sent')

            except Exception as e:
                print(e)
                speak('sir im not able to send this email')

        elif 'exit' in query:
            speak('ok sir')
            exit() 
        
        