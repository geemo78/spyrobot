
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

receiverEmail = "gioandrei140@gmail.com"
senderEmail = "spyrobot623@gmail.com"
subject = "SPYROBOT ALERT!!!"
 
myMessage = MIMEMultipart()
myMessage["From"] = senderEmail
myMessage["To"] = receiverEmail
myMessage["Subject"] = subject

def fireMail(imageName):
    # Add body to email
    body = "Warning! Fire has been detected!"
    myMessage.attach(MIMEText(body, "plain"))

    # We assume that the file is in the directory where you run your Python script from
    with open(imageName, "rb") as attachment:
        part = attachment.read()

    # Add attachment to your message and convert it to string
    imgAttach = MIMEImage(part, name=os.path.basename(imageName))

    myMessage.attach(imgAttach)
    mailTime = myMessage.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(senderEmail, 'lvwzrnlvcwkmjihq')
    server.sendmail(senderEmail, receiverEmail,mailTime)
    print("sent to {}".format(receiverEmail))
    server.close()

def send_sms_function():
    print('HELLO this is a message from spyrobot')

if __name__ == "__main__":
    fireMail("firegirl.jpg") 
