import pyttsx3
import speech_recognition as sr
import time
WIT_AI_KEY = "WIXQK777FRLYHPVXXD7M5Z4WCK2SBLS7"
r = sr.Recognizer()
engine = pyttsx3.init()
localtime = time.asctime(time.localtime(time.time()))
greeting = ["Hello" , "hi" , "how are" , "How are", "Hi" , "hello", "hey", "Hey"]
goodbye = ["Bye" , "goodbye" , "tata" , "bye" , "see you"]
fine = ["fine" , "Fine" , "good", "Good", "nice"]
Time = ["time", "Time" , "TIME"]

def time():
    data = localtime.split()
    justtime = data.pop(3)
    engine.say("The time is:")
    engine.runAndWait()
    engine.say(justtime)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print ("Listening...")
        #audio = r.listen(source)
        audio = r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.record(source, duration=3)
        text = r.recognize_wit(audio, key=WIT_AI_KEY)
    return text
    
welome = "Welcome to Baymax your personal digital assistant!"
engine.setProperty('rate' , 150)
engine.say(welome)
engine.runAndWait()
engine.setProperty('rate', 200)
engine.say("We use speech recognition system from  GOOGLE and Wit.Ai")
engine.runAndWait()
engine.setProperty('rate' , 150)
engine.say("Please enter your name:")
engine.runAndWait()
name = input("VULCAN -> Please enter your name: ")
question = name + ":  "
welcome1 = "Hello " + name 
engine.say(welcome1)
engine.runAndWait()
while(1):
    print (question)
    string = listen()
    print ("You said: " + string)
    data = string.split()
    for temp in data:
        for i in greeting:
            if(temp == i):
                engine.say("Hello! How are you?")
                engine.runAndWait()
        for j in goodbye:
            if(temp == j):
                engine.say("Goodbye! It was a pleasure serving you")
                engine.runAndWait()
                exit()
        for k in fine:
            if(temp == k):
                engine.say("Good to know. How can i help you?")
                engine.runAndWait()
        for l in Time:
            if(temp == l):
                time()