import pyttsx3

def text_to_speak(text , filename):
    engine = pyttsx3.init()
    engine.save_to_file(text , filename)
    engine.runAndWait()
    print(f"Audio Save in : {filename}")

filename = input("Enter File Name (.mp3 OR .wav) : ")
text = input("Enter Text : ")

text_to_speak(text , filename)