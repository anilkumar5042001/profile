from ..DAL.ShareProfileDAL import ShareProfileDAL
import smtplib 
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

class ShareProfileBAL:
    def ShareProfileInsert(self,ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message):
        randomNum = datetime.datetime.now().strftime("%d%m%Y%H%M%S%f")
        profileLink=ProfileLink+"/"+randomNum
        objShareProfileBAL=ShareProfileBAL()
        objShareProfileBAL.SendMail(EmailId,profileLink,Message)
        objShareProfileDAL=ShareProfileDAL()
        return objShareProfileDAL.ShareProfileInsert(ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message)

    def SendMail(self,toEmail,profileLink,userMessage):
        
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        msg = MIMEMultipart('alternative')
        
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login("anilkumar5042001@gmail.com", "") 
        
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
