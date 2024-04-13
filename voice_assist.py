import speech_recognition as sr
import pyttsx3
#pip install pyaudio
#pip install SpeechRecognition
#pip install pyttsx3
def listen_command():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm unable to access the Google API. Please check your internet connection.")
        return ""

def speak(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen_command()
        
        if "exit" in command:
            speak("Goodbye!")
            break
        
        # Add your command processing logic here
        # For example:
        if "hello" in command:
            speak("Hi there!")
        elif "how are you" in command:
            speak("I'm doing well, thank you for asking!")
        else:
            speak("I'm sorry, I didn't understand that command.")



