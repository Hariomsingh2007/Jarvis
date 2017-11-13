'''
Author : Hari om Singh
Date : 06-June -2017
Description: This will convert the Text to Audio
'''

from gtts import gTTS
import os
import pygame.mixer
from time import sleep

def text_to_audio(text):
    translate=gTTS(text=text ,lang='en')
    translate.save('chatbot.wav')
    pygame.mixer.init()

    path_name=os.path.realpath('chatbot.wav')
    real_path=path_name.replace('\\','\\\\')
    pygame.mixer.music.load(open(real_path,"rb"))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(1)

