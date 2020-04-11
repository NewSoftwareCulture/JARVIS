import os
import time
import speech_recognition as sr
import fuzzywuzzy
import datetime
from my_modules.speech import talk

opts = {
    "alias": ('кеша'),
    "tbr": ('скажи'),
    "cmds": {}
}

r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    print("Скажи что-нибудь ...")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print("Вы сказали: " + query.lower())