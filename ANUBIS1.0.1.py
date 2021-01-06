#-*- coding: utf-8 -*-
import wolframalpha
import wikipedia
import pyautogui
import webbrowser
import os
import phonenumbers
from phonenumbers import geocoder
from currency_converter import CurrencyConverter
import PyCurrency_Converter
import pyjokes
import sys
import time
import vlc
import pafy
pyautogui.alert("Hello I'm ANUBIS,powered by WOLFRAM|ALPHA")

Dec1=pyautogui.prompt("How may I help you? Enter 'Ask question' to access WOLFRAM. Enter 'Open wikipedia' to access wikipedia. Enter 'Enter website URL' to open URL. Enter 'Track number' to find the phone number's location. Enter 'Get geeky jokes' for a nerdy joke. Enter 'Set reminder' to set reminder. Enter 'Download on Youtube' to access YouTube.")#Enter input for application to open
Dec1=str(Dec1)

if Dec1=="Ask question":#Opens wolfram
    spam=pyautogui.prompt("Write your question here:")
    f_o_r=1
    app_id="VH4PQ6-U2KA6H32J8"
    client =wolframalpha.Client(app_id)
    res=client.query(spam)
    answer = next(res.results).text
    pyautogui.alert(answer)

elif Dec1=="Open wikipedia":#Opens wikipedia
    Wikipedia_info=pyautogui.prompt("Enter topic to be serached here on WIKIPEDIA:")
    pyautogui.alert(wikipedia.summary(Wikipedia_info,sentences=500))

elif Dec1=="Open URL:":#Opens URL
    website_open=pyautogui.prompt("Enter website URL")
    webbrowser.open(website_open)
elif Dec1=="Track number":
    X=pyautogui.prompt("Enter number here")
    phone_number1=phonenumbers.parse(X)
    pyautogui.alert(geocoder.description_for_number(phone_number1,"en"))

elif Dec1=="Get geeky jokes":
    pyautogui.alert(pyjokes.get_joke())
elif Dec1=="Dev info":
    pyautogui.alert("ANUBIS was made by Sachit Ramesh, a 16 year old tech enthusiast. The code is free and Open Source so feel to contribute on GitHub")
elif Dec1=="EASTER EGG!!!":
     pyautogui.alert("¯\_(ツ)_/¯  NOTHING HERE HUMAN!")
elif Dec1=="Set reminder":
    Reminder=pyautogui.prompt("What should I remind you about?")
    Time1=pyautogui.prompt("In how many minutes?")
    Time1=float(Time1)
    Time1=Time1*60
    time.sleep(Time1)
    pyautogui.alert("REMINDER!!!")
    pyautogui.alert(Reminder)
elif Dec1=="Download from Youtube":
    url=pyautogui.prompt("Enter video URL to watch without ads and in best quality.")
    video=pafy.new(url)
    best =video.getbest()
    media=vlc.MediaPlayer(best.url)
    media.play()
else:
    pyautogui.alert("Invalid Command...:p,Ciao!")
pyautogui.alert("Thank you for downloading ANUBIS, as we are a growing Non-profit free software please do consider donating to ANUBIS,for more info write to us @quantechlxxi.corp@gmail.com -ANUBIS developer")
