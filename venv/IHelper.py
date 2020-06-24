import speech_recognition as sr
import os
import sys
import pyttsx3
import webbrowser

def talk(words):
  engine = pyttsx3.init()
  engine.say(words)
  engine.runAndWait()

def command():
  r= sr.Recognizer()

  with sr.Microphone() as source:
       print("talkd")
       r.pause_threshold=1
       r.adjust_for_ambient_noise(source, duration=1)
       audio=r.listen(source)

  try:
    task = r.recognize_google(audio).lower()
    print("you said " + command)
  except sr.UnknownValueError:
    talk("I do not understand")
    task = command()

  return task

def makeSomething (task):
  if 'open website' in task:
    talk("open website")
    url= "https://google.com"
    webbrowser.open(url)
  elif 'stop' in task:
    talk("ok")
    sys.exit()

while True:
  makeSomething(command())