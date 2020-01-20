from ..DAL.ShareProfileDAL import ShareProfileDAL
import smtplib 

class ShareProfileBAL:
    def ShareProfileInsert(self,ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message):
        objShareProfileDAL=ShareProfileDAL()
        return objShareProfileDAL.ShareProfileInsert(ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message)

    def SendMail(self):
        a="abc"
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login("anilkumar5042001@gmail.com", "password") 
        
        # message to be sent 
        message = "Message_you_need_to_send"
        
        # sending the mail 
        s.sendmail("anilkumar5042001@gmail.com", "anilkumar5042001@gmail.com", message) 
        
        # terminating the session 
        s.quit()
