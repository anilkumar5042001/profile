import smtplib 
import random
import email.message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import string
from ..Helper.EmailTemplate import *

class CommonMethodsBAL:
  

    def SendActivationEmail(self,toEmail,profileLink,activationCode):
        objEmailTemplate=EmailTemplate()
        activationEmailTemplate=objEmailTemplate.GetActivationEmail(profileLink,activationCode)

        msg = email.message.Message()
        msg['Subject'] = 'Worked Activate Account'
        msg['From'] = 'anil.spnet@gmail.com'
        msg['To'] = toEmail
        msg.add_header('Content-Type','text/html')
        
        # msg.set_payload('Body of <p>Dear User,</p><p>Please click</p>')
        msg.set_payload(activationEmailTemplate)

        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls()
        s.login("anil.spnet@gmail.com", "sumalatha") 
        s.sendmail(msg['From'], toEmail, msg.as_string())
        s.quit()

    def SendMail(self,toEmail,subject,htmlBody):
        msg = email.message.Message()
        msg['Subject'] = subject
        msg['From'] = 'anil.spnet@gmail.com'
        msg['To'] = toEmail
        msg.add_header('Content-Type','text/html')
        msg.set_payload(htmlBody)

        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls()
        s.login("anil.spnet@gmail.com", "sumalatha") 
        s.sendmail(msg['From'], toEmail, msg.as_string())
        s.quit()


   