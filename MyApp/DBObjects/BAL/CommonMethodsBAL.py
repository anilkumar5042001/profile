import smtplib 
import random
import email.message
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

    def SendHTMLMail(self,toEmail,profileLink,userMessage):
        
        msg = email.message.Message()
        msg['Subject'] = 'foo'
        msg['From'] = 'anil.spnet@gmail.com'
        msg['To'] = toEmail
        msg.add_header('Content-Type','text/html')
        msg.set_payload('Body of <p><b>message</b></p><p>Please click</p>')

        # Send the message via local SMTP server.
        #s = smtplib.SMTP('localhost')
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        # msg = MIMEMultipart('alternative')
            
        #     # start TLS for security 
        # s.starttls() 
            
        # Authentication 
       
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        # s.sendmail("anil.spnet@gmail.com", toEmail, msg.as_string())
        # s.quit()

        # Send the message via local SMTP server.
        s.starttls()
        s.login("anil.spnet@gmail.com", "sumalatha") 
        s.sendmail(msg['From'], toEmail, msg.as_string())
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