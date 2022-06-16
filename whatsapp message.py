import pywhatkit
from datetime import datetime
now=datetime.now()
chour=now.strftime("%H")
phoneno=input("Enter the Mobile No of the receiver :")
message=input("Enter the Message :")
hour=int(input("Enter hour :"))
minute=int(input("Enter minute :"))

pywhatkit.sendwhatmsg(phoneno,message,hour,minute)
