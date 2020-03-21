import smtplib 
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import string

class CommonMethodsBAL:
    def SendMail(self,toEmail,profileLink,userMessage):
        
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        msg = MIMEMultipart('alternative')
        
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login("anil.spnet@gmail.com", "sumalatha") 
        
        # message to be sent 
        message = "<html><body>"
        message+="Please click on the below link to access link"
        message+="<a href='"+profileLink+"'>Click here</a></br>"
        message+="<p>"+userMessage+"</p>"
        message+="</body></html>"
        
        part2 = MIMEText(message, 'html')
        SUBJECT="Work Profile"
        mailMessage = 'Subject: {}\n\n{}'.format(SUBJECT, message)
        
        # sending the mail 
        s.sendmail("anil.spnet@gmail.com", toEmail, mailMessage) 
    
        # terminating the session
        s.quit()

    def SendMailWithSubject(self,toEmail,profileLink,userMessage):
        
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        msg = MIMEMultipart('alternative')
        
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login("anil.spnet@gmail.com", "sumalatha") 
        
        # message to be sent 
        message = "<html><body>"
        message+="Please click on the below link to access link"
        message+="<a href='"+profileLink+"'>Click here</a></br>"
        message+="<p>"+userMessage+"</p>"
        message+="</body></html>"
        
        part2 = MIMEText(message, 'html')
        
        # sending the mail 
        s.sendmail("anilkumar5042001@gmail.com", toEmail, message) 
    
        # terminating the session
        s.quit()