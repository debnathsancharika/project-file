import pyttsx3
import os
import smtplib

pyttsx3.speak("Welcome to my assistant ")


#print("Press 1: to open notepad")

while True:
	pyttsx3.speak("How can I help you ?")
	print("Enter your choice : " , end=" ")
	p=input()
	#Alexa-Holes
	
	if   (("notepad" in p)or ("editor" in p)):
		pyttsx3.speak("Opening Notepad")
		os.system("notepad")
		pyttsx3.speak("Done")
	elif  (("chorme" in p)or ("google" in p)):
		pyttsx3.speak("Opening google chrome")
		os.system("start chrome ")
		pyttsx3.speak("Done")
	elif  (("facebook" in p)or ("fb" in p)):
		pyttsx3.speak("Opening facebook")
		os.system("start chrome www.facebook.com")
		pyttsx3.speak("Done")
	elif  (("instagram" in p)or ("insta" in p)):
		pyttsx3.speak("Opening instagram")
		os.system("start chrome www.instagram.com")
		pyttsx3.speak("Done")
	elif  (("youtube" in p)or ("utube" in p)):
		pyttsx3.speak("Opening youtube")
		os.system("start chrome www.youtube.com")
		pyttsx3.speak("Done")
	elif  (("window media player" in p)or ("wmplayer" in p)):
		pyttsx3.speak("Opening window media player")
		os.system("start wmplayer")
		pyttsx3.speak("Done")
	elif  (("alarm" in p)or ("clock" in p)):
		pyttsx3.speak("Opening Alarms & Clock")
		os.system("start  Alarms & Clock")
		pyttsx3.speak("Done")
	elif  (("calculator" in p)or ("cal" in p)):
		pyttsx3.speak("Opening calculator")
		os.system("start  calculator")
		pyttsx3.speak("Done")
	elif  (("microsoft edge" in p)or ("edge" in p)):
		pyttsx3.speak("Opening microsoft edge")
		os.system("start  microsoft edge")
		pyttsx3.speak("Done")
	elif  (("spotify" in p)or ("music" in p)):
		pyttsx3.speak("Opening spotify")
		os.system("start  Spotify")
		pyttsx3.speak("Done")
	elif  (("stremio" in p)or ("movie" in p)):
		pyttsx3.speak("Opening stremio")
		os.system("start  Stremio+4.4.77")
		pyttsx3.speak("Done")
	elif  (("telegram" in p)or ("telegram desk" in p)):
		pyttsx3.speak("Opening telegram desktop")
		os.system("start  telegram desktop")
		pyttsx3.speak("Done")
	elif  (("vlc" in p)or ("vlc media player" in p)):
		pyttsx3.speak("Opening vlc media player")
		os.system("start  vlc media player")
		pyttsx3.speak("Done")
	elif  (("whatsapp" in p)or ("wtsapp" in p)):
		pyttsx3.speak("Opening whatsapp")
		os.system("start  whatsapp")
		pyttsx3.speak("Done")
	elif  (("wps" in p)or ("wps office" in p)):
		pyttsx3.speak("Opening wps office")
		os.system("start  wps office")
		pyttsx3.speak("Done")
	elif  (("zoom" in p)or ("zoom meeting" in p)):
		pyttsx3.speak("Opening zoom meeting")
		os.system("start  zoom ")
		pyttsx3.speak("Done")
	elif  (("team viewer" in p)) :
		pyttsx3.speak("Opening team viewer")
		os.system("start  team viewer")
		pyttsx3.speak("Done")
	elif  (("team viewer" in p)) :
		pyttsx3.speak("Opening team viewer")
		os.system("start  team viewer")
		pyttsx3.speak("Done")
	elif  (("email" in p) or ("gmail" in p)):
        	pyttsx3.speak("opening gmail")
        	os.system("start chrome https://mail.google.com/mail/")
		#pyttsx3.speak("Done")
	elif ("exit" in p) or ("quit" in p):
		pyttsx3.speak("good bye, have a nice day")
		break
	else :
		print("Not support")
		pyttsx3.speak("sorry ! I can't understand you ")
# os.system(p)