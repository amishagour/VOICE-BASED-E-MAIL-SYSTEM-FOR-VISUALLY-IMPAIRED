import speech_recognition as sr
import smtplib
from bs4 import BeautifulSoup
from gtts import gTTS
import os, time
import pyttsx3
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import sys
engine = pyttsx3.init() 
voice = engine.getProperty('voices')
engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\
Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)
def speak(sentence):
 engine.say(sentence)
 engine.runAndWait()
 def listen(sen):
 r = sr.Recognizer() 
 with sr.Microphone() as source: 
 speak(sen)
 print("listening...")
 audio = r.record(source,duration=5)
 try:
 str=r.recognize_google(audio)
 return str
 except sr.UnknownValueError:
 listen("Sorry I did not understand what you said. Can you please repeat...")
 except sr.RequestError as e:
 print("Could not request results; {0}".format(e))
 except:
 speak("We are not connected to the internet")
 sys.exit()
print("Voice Based Email System for Visually Impaired")
speak("Voice based email system for Visually Impaired")
while(True):
 print ("1. Compose a mail.")
 speak("option 1. compose a mail.")
 print ("2. Check your inbox")
 speak("option 2. Check your inbox")
 print ("3. Exit")
 speak("option 3. Exit")
 #this is for input choices
 text=listen("Tell your option number")
 print("You said: "+text)
 #choices details
 if (('1' in text) or ('One' in text) or ('one' in text) or ('compose a mail' in text) or 
('compose' in text) or ('open compose' in text)):
 while(True):
 print (" To whom you want to send the mail")
 #this is for input choices
 text=listen("To whom you want to send the mail")
 print("You said: "+text)
 if (('Harshini' in text) or ('harshini' in text) or ('harshani' in text)):
 #print("Tell your subject:")
 audio1=listen("Tell your subject:")
 print("Your subject is : "+audio1)
 speak("Your subject is "+audio1)
 print ("Tell your message :")
 audio2=listen("Tell your message:")
 print("Your message:"+audio2)
 speak("Your message is "+audio2)
 mail = smtplib.SMTP('smtp.gmail.com',587) #host and port area
 mail.ehlo() #Hostname to send for this command defaults to the FQDN of the 
local host.mail.starttls() #security connection
 mail.login('romanoffrogers21@gmail.com','as0310&pi1719') #login part
 
mail.sendmail('romanoffrogers21@gmail.com','Harshini.b.3107@gmail.com',msg) #send 
part
 print ("Congrats! Your mail has been sent. ")
 speak("Congrats! Your mail has been sent. ")
 mail.close()
 break
 elif (('abhinav' in text) or ('Abhinav' in text) or ('abhi' in text) or ('abhinan' in 
text)) :
 #print("Tell your subject:")
 audio1=listen("Tell your subject:")
 print("Your subject is : "+audio1)
 speak("Your subject is "+audio1)
 print ("Tell your message :")
 audio2=listen("Tell your message:")
 print("Your message:"+audio2)
 speak("Your message is "+audio2)
 mail = smtplib.SMTP('smtp.gmail.com',587) #host and port area
 mail.ehlo() #Hostname to send for this command defaults to the FQDN of the 
local host.
 mail.starttls() #security connection
 mail.login('romanoffrogers21@gmail.com','as0310&pi1719') #login part
  
mail.sendmail('romanoffrogers21@gmail.com','konakalaabhinav@gmail.com',msg) 
#send part
 print ("Congrats! Your mail has been sent. ")
 speak("Congrats! Your mail has been sent. ")
 mail.close()
 break
 elif (('Amisha' in text) or ('amisha' in text) or ('amisa' in text) or ('Amisha' in text) 
or ('Tree' in text)) :
 #print("Tell your subject:")
 audio1=listen("Tell your subject:")
 print("Your subject is :"+audio1)
 speak("Your subject is "+audio1)
 print ("Tell your message :")
 audio2=listen("Tell your message:")
 print("Your message:"+audio2)
 speak("Your message is "+audio2)
 mail = smtplib.SMTP('smtp.gmail.com',587) #host and port area
 mail.ehlo() #Hostname to send for this command defaults to the FQDN of the 
local host.
 mail.starttls() #security connection
 mail.login('romanoffrogers21@gmail.com','as0310&pi1719') #login part
 
mail.sendmail('romanoffrogers21@gmail.com','amishagour1207@gmail.com',msg) #send 
part
 print ("Congrats! Your mail has been sent. ")
 speak("Congrats! Your mail has been sent. ")
 mail.close()
 break
 elif (('harshini and amisha' in text) or ('amisha and harshini' in text) or ('harshani 
and amisa' in text)) :
 #print("Tell your subject:")
 audio1=listen("Tell your subject:")
 print("Your subject is :"+audio1)
 speak("Your subject is "+audio1)
 print ("Tell your message :")
 audio2=listen("Tell your message:")
 print("Your message:"+audio2)
 speak("Your message is "+audio2)
 mail = smtplib.SMTP('smtp.gmail.com',587) #host and port area
 mail.ehlo() #Hostname to send for this command defaults to the FQDN of the 
local host.
 mail.starttls() #security connection
 mail.login('romanoffrogers21@gmail.com','as0310&pi1719') #login part
 
mail.sendmail('romanoffrogers21@gmail.com','harshini.b.3107@gmail.com',msg)
 
mail.sendmail('romanoffrogers21@gmail.com','amishagour1207@gmail.com',msg) #send 
part
 print ("Congrats! Your mail has been sent. ")
 speak("Congrats! Your mail has been sent. ")
 mail.close()
 break
 elif (('harshini and abhinav' in text) or ('harshani and abhinan' in text) or 
('abhinav and harshini' in text)) :
 #print("Tell your subject:")
 audio1=listen("Tell your subject:")
 print("Your subject is : "+audio1)
 speak("Your subject is "+audio1)
 print ("Tell your message :")
 audio2=listen("Tell your message:")
 print("Your message:"+audio2)
 speak("Your message is "+audio2)
 mail = smtplib.SMTP('smtp.gmail.com',587) #host and port area
 mail.ehlo() #Hostname to send for this command defaults to the FQDN of the 
local host.
 mail.starttls() #security connection
 mail.login('romanoffrogers21@gmail.com','as0310&pi1719') #login part
 
mail.sendmail('romanoffrogers21@gmail.com','harshini.b.3107@gmail.com',msg)
 
mail.sendmail('romanoffrogers21@gmail.com','konakalaabhinav@gmail.com',msg) #send 
part
 print ("Congrats! Your mail has been sent. ")
 speak("Congrats! Your mail has been sent. ")
 mail.close()
 break
 elif (('amisha and abhinav' in text) or ('abhinav and amisha' in text) or ('abhinav 
and amisa' in text) or ("amisa and abhinan" in text)) :
 #print("Tell your subject:")
 audio1=listen("Tell your subject:")
 print("Your subject is : "+audio1)
 speak("Your subject is "+audio1)
 print ("Tell your message :")
 audio2=listen("Tell your message:")
 print("Your message:"+audio2)
 speak("Your message is "+audio2)
 mail = smtplib.SMTP('smtp.gmail.com',587) #host and port area
 mail.ehlo() #Hostname to send for this command defaults to the FQDN of the 
local host.
 mail.starttls() #security connection
 mail.login('romanoffrogers21@gmail.com','as0310&pi1719') #login part
 
mail.sendmail('romanoffrogers21@gmail.com','amishagour1207@gmail.com',msg)
 
mail.sendmail('romanoffrogers21@gmail.com','konakalaabhinav@gmail.com',msg) #send 
part
 print ("Congrats! Your mail has been sent. ")
 speak("Congrats! Your mail has been sent. ")
 mail.close()
 break
 elif (("to all" in text.lower())) :
 #print("Tell your subject:")
 audio1=listen("Tell your subject:")
 print("Your subject is : "+audio1)
 speak("Your subject is "+audio1)
 print ("Tell your message :")
 audio2=listen("Tell your message:")
 print("Your message:"+audio2)
 speak("Your message is "+audio2)
 mail = smtplib.SMTP('smtp.gmail.com',587) #host and port area
 mail.ehlo() #Hostname to send for this command defaults to the FQDN of the 
local host.
 mail.starttls() #security connection
 mail.login('romanoffrogers21@gmail.com','as0310&pi1719') #login part
 
mail.sendmail('romanoffrogers21@gmail.com','harshini.b.3107@gmail.com',msg)
 
mail.sendmail('romanoffrogers21@gmail.com','konakalaabhinav@gmail.com',msg) #send 
part
 
mail.sendmail('romanoffrogers21@gmail.com','amishagour1207@gmail.com',msg)
 print ("Congrats! Your mail has been sent. ")
 speak("Congrats! Your mail has been sent. ")
 mail.close()
 break
 else:
 speak(" Sorry No such name exists!")
 elif (('2' in text) or ('tu' in text) or ('two' in text) or ('Tu' in text) or ('to' in text) or 
('To' in text) or ('check inbox' in text) or ('inbox' in text)) :
 username = "romanoffrogers21@gmail.com"
 password = "as0310*******"
 # create an IMAP4 class with SSL 
 imap = imaplib.IMAP4_SSL("imap.gmail.com")
 imap.login(username, password)
 status, messages = imap.select("INBOX")
 # number of top emails to fetch
 N = 1
 speak("reading the recent email from your inbox")
 for i in range(messages, messages-N, -1):
 # fetch the email message by ID
 res, msg = imap.fetch(str(i))
 for response in msg:
 if isinstance(response, tuple):
 msg = email.message_from_bytes(response[1])
 if isinstance(subject, bytes):
 # if it's a bytes, decode to str
 subject = subject.decode(encoding)
 # decode email sender
 From, encoding = decode_header(msg.get("From"))[0]
 print("Subject:", subject)
 speak("subject: "+subject)
 print("From:", From)
 speak("From: "+str(From))
 try:
 # get the email body
 body = part.get_payload(decode=True).decode()
 except:
 pass
 if content_type == "text/plain" and "attachment" not in 
content_disposition:
 print(body)
 speak(body)
 elif "attachment" in content_disposition:
 filename = part.get_filename()
 if filename:
 folder_name = check(subject)
 if not os.path.isdir(folder_name):
 # make a folder for this email (named after the subject)
 os.mkdir(folder_name)
 filepath = os.path.join(folder_name, filename)
 print("the file is saved "+filepath)
 speak("the file is saved "+filepath)
 else:
 content_type = msg.get_content_type()
 # get the email body
 body = msg.get_payload(decode=True).decode()
 if content_type == "text/plain":
 print(body)
 speak(body)
 # close the connection and logout
 imap.close()
 imap.logout()
 elif(("3" in text) or ("three" in text.lower()) or ("exit" in text.lower()) or ("sign out" in 
text.lower()) ):
 speak("Thank you for using Voice based email system for blind")
 speak("goodbye!")
 sys.exit()
 else:
 speak("Invalid input can you please repeat")
