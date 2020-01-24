from ..DAL.ShareProfileDAL import ShareProfileDAL
import smtplib 
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import string

class ShareProfileBAL:
    def ShareProfileInsert(self,ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message):
        # strEmailIds='anilkumar5042001@gmail.com;riav4562001@gmail.com'
        splitEmailIds= EmailId.split(";")
        lensplitEmailIds=len(EmailId.split(';'))

        for x in range(0,lensplitEmailIds):
            email=splitEmailIds[x]
            randomNum = datetime.datetime.now().strftime("%d%m%Y%H%M%S%f")
            profileLink=ProfileLink+"/"+randomNum
            objShareProfileBAL=ShareProfileBAL()
            objShareProfileBAL.SendMail(email,profileLink,Message)
            objShareProfileDAL=ShareProfileDAL()
            objShareProfileDAL.ShareProfileInsert(ProfileId,email,randomNum,ExpiryDate,SharedWith,Message)
        return "1"

    def ShareProfileGetProfileIdByProfileLink(self,profileLink):
        objShareProfileDAL=ShareProfileDAL()
        return objShareProfileDAL.ShareProfileGetProfileIdByProfileLink(profileLink) 

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
        s.sendmail("anilkumar5042001@gmail.com", toEmail, mailMessage) 
    
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