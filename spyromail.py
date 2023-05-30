
import smtplib

recipientEmail = "gioandrei140@gmail.com"
senderEmail = "spyrobot623@gmail.com"

def send_mail_function():

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(senderEmail, 'lvwzrnlvcwkmjihq')
        server.sendmail(senderEmail, recipientEmail, "Warning A Fire Accident has been reported")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
    	print(e)

def send_sms_function():
    print('hello')


send_mail_function()