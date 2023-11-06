import pyttsx3
import random, time



engine = pyttsx3.init()
voices = engine.getProperty('voices')
i=0
for voice in voices:
    print(voice)
    print(voice.id+" : "+str(i))
    i+=1
time.sleep(1)
# Esto nos permite escoger la voz la que utilizara el  asistente virtual...
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[21].id) # Escogimos como voz Spanish Latin, escoger el idioma.
##LISTA //poner URL PORFA
##engine.setProperty('lang', 'es')
# ... Esto nos permitira escoger la voz que utilizara el asistente virtual.


words = ['Sexo', 'en', 'el', 'oxxo', 'sexoooooooo','eeen']     
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)  
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
  
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
  
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
  
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
  
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
  
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)
engine.say(random.choice(words))
engine.runAndWait()
time.sleep(0.3)

