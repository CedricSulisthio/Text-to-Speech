# Text to Speech (1)

import pyttsx3 
engine = pyttsx3.init()

def speakText(command):
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.say(command) 
    engine.runAndWait()
    engine.stop()

def save(text, fName='test.mp3'):
    engine.save_to_file(text, fName)
    engine.runAndWait()
    
    # rate = engine.getProperty('rate')  # Current speaking rate
    # engine.setProperty('rate', 355)  # Set up new voice rate
    # rate = engine.getProperty('rate')  # New speaking rate
    # print(rate)  # Printing new voice rate

    # volume = engine.getProperty('volume')  # Current volume
    # print(volume)  # Current volume level
    # engine.setProperty('volume', 1.0)  # Setting up volume level between 0 and 1

if __name__ == "__main__":
    command = "Welcome to my world"
    speakText(command)
    save(command)

    voices = engine.getProperty('voices')
    for k,v in enumerate(voices):
        print(k,v)
    engine.setProperty('voice', voices[1].id)