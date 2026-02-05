import pyttsx3
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def set_reminder():
    speak("Reminder set for five seconds")
    time.sleep(5)
    speak("This is your reminder")

def read_news():
    speak("Here is today's news")
    speak("Artificial intelligence is growing very fast")

def main():
    speak("Hello Friends, how can I help you?")
    
    while True:
        command = input("Type command (news / reminder / exit): ").lower()

        if "reminder" in command:
            set_reminder()

        elif "news" in command:
            read_news()

        elif "exit" in command:
            speak("Goodbye")
            break

main()
