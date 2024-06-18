import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text to speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("User said:", query)
            return query.lower()
        except Exception as e:
            print("Sorry, I couldn't understand. Can you repeat?")
            return ""

# Function to perform tasks based on voice commands
def perform_task(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak("Today is " + current_date)
    elif "search" in command:
        speak("What do you want me to search for?")
        search_query = recognize_speech()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query
            webbrowser.open(url)
            speak("Here are the search results for " + search_query)
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I didn't catch that.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            perform_task(command)
