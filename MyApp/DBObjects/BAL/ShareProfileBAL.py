from ..DAL.ShareProfileDAL import ShareProfileDAL
import smtplib 
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import string
from ..Helper.EmailTemplate import *
from .CommonMethodsBAL import *
from ...GlobalConstants import *
from .UserProfileBAL import *

class ShareProfileBAL:
    def ShareProfileInsert(self,ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message,ShareType):
        # strEmailIds='anilkumar5042001@gmail.com;riav4562001@gmail.com'
        randomNum="1"
        if(ShareType=="Email"):
            splitEmailIds= EmailId.split(";")
            lensplitEmailIds=len(EmailId.split(';'))
            objUserProfileBAL=UserProfileBAL()
            objUserEntity=objUserProfileBAL.GetUserProfileById(ProfileId)
            userFullName=objUserEntity.FirstName+" "+objUserEntity.LastName

            for x in range(0,lensplitEmailIds):
                email=splitEmailIds[x]
                randomNum = datetime.datetime.now().strftime("%d%m%Y%H%M%S%f")
                profileLink=ProfileLink+"/"+randomNum
                objShareProfileBAL=ShareProfileBAL()
                objShareProfileBAL.SendShareProfileEmail(email,profileLink,userFullName,Message,ExpiryDate)
                objShareProfileDAL=ShareProfileDAL()
                objShareProfileDAL.ShareProfileInsert(ProfileId,email,randomNum,ExpiryDate,SharedWith,Message,ShareType)
        elif (ShareType=="Link"):
            randomNum = datetime.datetime.now().strftime("%d%m%Y%H%M%S%f")
            objShareProfileDAL=ShareProfileDAL()
            objShareProfileDAL.ShareProfileInsert(ProfileId,EmailId,randomNum,ExpiryDate,SharedWith,Message,ShareType)
            
        return randomNum

    def SendShareProfileEmail(self,emailId,profileLink,userFullName,msg,ExpiryDate):
        objCommonMethodsBAL=CommonMethodsBAL()
        objEmailTemplate=EmailTemplate()
        objGlobalConstants=GlobalConstants()
        strExpiryDate = ExpiryDate.split('-')
        strFormattedDate =strExpiryDate[2]+"-"+strExpiryDate[1]+"-"+strExpiryDate[0]
        shareProfileEmailTemplate=objEmailTemplate.GetShareProfileEmail(profileLink,msg,userFullName,strFormattedDate)
        subject="Profile link: "+userFullName
        objCommonMethodsBAL.SendMail(emailId,subject,shareProfileEmailTemplate)

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