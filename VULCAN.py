import pyttsx3
import speech_recognition as sr
import time

WIT_AI_KEY = "WIXQK777FRLYHPVXXD7M5Z4WCK2SBLS7"
r = sr.Recognizer()
engine = pyttsx3.init()
localtime = time.asctime(time.localtime(time.time()))


greeting = ["Hello" , "hi" , "how are" , "How are", "Hi" , "hello", "hey", "Hey"]
goodbye = ["Bye" , "goodbye" , "tata" , "bye" , "see you", "thank"  ]
fine = ["fine" , "Fine" , "good", "Good", "nice"]
Time = ["time", "Time" , "TIME"]


def time():
    data = localtime.split()
    justtime = data.pop(3)
    say("The time is:")
    say(justtime) 
def listen():
    with sr.Microphone() as source:
        print ("Listening...")
        #audio = r.listen(source)
        audio = r.adjust_for_ambient_noise(source, duration=0.5)
        r.energy_threshold = 4000
        audio = r.record(source, duration=3)
        text = r.recognize_wit(audio, key=WIT_AI_KEY)
    return text
def say(s):
    engine.setProperty('rate' , 150)
    engine.say(s)
    engine.runAndWait() 
def sayfast(s):
    engine.setProperty('rate', 200)
    engine.say(s)
    engine.runAndWait()


say("Welcome to Beymax your personal digital assistant!")
sayfast("We use speech recognition system from  GOOGLE and Wit.Ai")
say("Please enter your name:")
name = input("BAYMAX -> Please enter your name: ")
question = name + ":  "
welcome1 = "Hello " + name 
say(welcome1)
while(1):
    print (question)
    string = listen()
    print ("You said: " + string)
    data = string.split()
    for temp in data:
        for i in greeting:
            if(temp == i):
                say("Hello! How are you?")
        for j in goodbye:
            if(temp == j):
                say("Goodbye! It was a pleasure serving you") 
                exit()
        for k in fine:
            if(temp == k):
                say("Good to know. I am good. How can i help you?")
        for l in Time:
            if(temp == l):
                time()
        