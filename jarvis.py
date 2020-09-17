import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
import requests
import wolframalpha
from urllib.request import urlopen
import time

engine = pyttsx3.init()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time_():
	time=datetime.datetime.now().strftime("%I:%M:%S")
	speak("The current time is")
	speak(time)

def date_():
	year=datetime.datetime.now().year
	month=datetime.datetime.now().month
	date=datetime.datetime.now().day
	speak(date)
	speak(month)
	speak(year)

def wishme():
	speak("welcome back TOM!")
	time_()
	date_()
	hour=datetime.datetime.now().hour
	if hour>=6 and hour<12:
		speak("GOOD MORNING TOM!!!")
	elif hour>=12 and hour<18:
		speak("GOOD AFTERNOON TOM!!!")
	elif hour>=18 and hour<24:
		speak("GOOD EVENING TOM!!!")
	else:
		speak("GOOD NIGHT TOM!!!")
	speak("Jarvis at your service and please tell me how can I help you???")

def TakeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 1
		audio=r.listen(source)
	try:
		print("Recognizing....")
		query=r.recognize_google(audio,language='en-US')
		print(query)
	
	except Exception as e:
		print(e)
		print("say that again please....")
		return "None"
	return query

def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('username@gmail.com','password')
	server.sendmail('username@gmail.com',to,content)
	server.close()

def cpu():
	usage=str(psutil.cpu_percent())
	speak('CPU is at'+usage)
	battery=psutil.sensors_battery()
	speak('Battery is at')
	speak(battery)

def joke():
	speak(pyjokes.get_joke())

def screenshot():
	img=pyautogui.screenshot()
	speak('Where do you want to save??? I mean which drive , You cant save in C drive unless you run me as admin ')
	drive=TakeCommand()
	img.save(drive+':\screenshot.png')
	speak('screenshot is saved in'+drive'drive')	

if __name__=="__main__":
	wishme()
	while True:
		query=TakeCommand().lower()

		if 'time' in query:
			time_()
		elif 'date' in query:
			date_()
		elif 'wikipedia' in query:
			speak("Searching........")
			query=query.replace('wikipedia','')
			result=wikipedia.summary(query,sentences=3)
			speak('According to wikipedia')
			print(result)
			speak(result)	
		elif 'send email' in query:
			try:
				speak("What should I say????")
				content=TakeCommand()
				speak("Who is the reciever???")
				reciever=input("Enter Reciever's Email")
				to=reciver
				sendEmail(to,content)
				speak(content)
				speak('Email has send')
			except Exception as e:
				print(e)
				speak("sorry unable to send email")
		
		elif 'search in chrome' in query:
			speak('what should I search???')
			search=TakeCommand().lower()
			wb.open(search+'.com')
		elif 'search in youtube' in query:
			speak('what should I search???')
			search=TakeCommand().lower()
			speak('searching')
			wb.open('https://www.youtube.com/results?search_query='+search)
		
		elif 'search in google' in query:
			speak('what should I search???')
			search=TakeCommand().lower()
			speak('searching')
			wb.open('https://www.google.com/search?q='+search)

		elif 'cpu' in query:
			cpu()
		elif 'joke' in query:
			joke()
		elif 'go offline' in query:
			speak('going offline sir!')
			quit()
		elif 'write a note' in query:
			speak("what should I write , sir???")
			notes=TakeCommand()
			file=open('notes.txt','w')
			speak("Sir should I include Date and Time??")
			ans=TakeCommand()
			if 'yes' in ans or 'sure' in ans:
				strTime=datetime.datetime.now().strftime("%I:%M:%S")
				file.write(strTime)
				file.write(':-')
				file.write(notes)
				speak('Done Taking Note, SIR!')
			else:
				file.write(notes)
		
		elif 'show note' in query:
			speak('showing notes')
			file=open('notes.txt','r')
			speak(str(file.read()))
			print(file.read())
					
		
	
		elif 'screenshot' in query:
			screenshot()	
			 
		elif 'play music' in query:
			songs_dir='E:\songs'
			speak('what should I play?')
			speak('select a number')
			ans=TakeCommand().lower()
			while('number' not in ans and ans!= 'you choose'):
				speak("I couldn't understand you , please say again")
				ans=TakeCommand().lower()
			if 'number' in ans:
				no=int(ans.replace('number',''))
			if 'random' or 'you choose' in ans:
				no=random.randint(1,100)
			os.startfile(os.path.join(songs_dir,music[no]))

		elif 'remember that' in query:
			speak('what should I remember???')
			memory=TakeCommand()
			speak("you aked me to remember that"+memory)
			remember=open('memory.txt','w')
			remember.write(memory)
			remember.close()

		
		elif 'do you remember anything' in query:
			remember=open('memory.txt','r')
			speak("you asked me to remember that"+str(remember.read()))
		
		elif 'news' in query:
			try:
				speak('Enter your Api')
				apiid=input('Enter your Api ')
				jsonObj=urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="+apiid)
				data=json.load(jsonObj)
				i=1
				speak('HERE ARE SOME TOP NEWS HEADLINES')
				for item in data['articles']:
					print(str(i)+'. '+item['title']+'\n')
					print(item['description']+'\n')
					speak(item['title'])
					i+=1
			except Exception as e:
				print(str(e))


		elif 'where is' in query:
			query=query.replace("where is","")
			location=query
			speak("User asked locate"+location)
			wb.open("https://www.google.com/maps/place/"+location)

		elif 'calculate' in query:
			speak('Enter your Api')
			wolframalpha_app_id=input('Enter your Api ')
			client=wolframalpha.Client(wolframalpha_app_id)
			indx=query.lower().split().index('calculate')
			query=query.split()[indx+1:]
			res=client.query(''.join(query))
			answer=next(res.results).text
			print('The Answer is : '+answer)
			speak('The Answer is : '+answer)
		elif 'what is' in query or 'who is' in query :
			speak('Enter your Api')
			wolframalpha_app_id=input(' Enter your Api ')
			client=wolframalpha.Client(wolframalpha_app_id)
			res=client.query(query)
			try:
				print(next(res.results).text)
				speak(next(res.results).text)
			except StopIteration:
				print("No Results")
		elif 'stop listening' in query:
			speak('For How many second you want me to stop obeying your commands SIR???')
			ans=int(TakeCommand())
			time.sleep(ans)
			print(ans)
		elif 'log out' in query:
			speak('system is going log out')
			os.system("shutdown -1")
		elif 'restart' in query:
			speak('system is going restart')
			os.system("shutdown /r /t 1")
		elif 'shutdown' in query:
			speak('system is going to shutdown')
			os.system("shutdown /s /t 1")
		elif 'who created you' in query or 'who made you' in query:
			speak('I was made by Tom Thomas')
		elif 'who are you' in query:
			speak('I am Jarvis an AI python proggram made by Tom Thomas')

