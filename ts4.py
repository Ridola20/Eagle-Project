import speech_recognition as sr

def listen():
    try:
        with sr.Microphone() as source2:
            j = sr.Recognizer()

            j.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = j.listen(source2)
            phrase = j.recognize_google(audio2)
            return phrase
        
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
        with sr.Microphone() as source2:
            j = sr.Recognizer()

            j.adjust_for_ambient_noise(source2, duration=9)

            audio2 = j.listen(source2)
            phrase = j.recognize_sphinx(audio2)
            return phrase
         
    except sr.UnknownValueError:
        main()
        
        

def main():
    while True:
        j = listen()
        f = open("Saved.txt", "a")
        f.write(j + ";")
        f.close()

main()