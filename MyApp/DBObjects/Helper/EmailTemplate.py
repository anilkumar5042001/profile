class EmailTemplate:
    def GetActivationEmail(self,profileLink,activationCode):
        message = "<p>Dear User,</p>"
        message +="<p>"
        message+="Please <a href='"+profileLink+"'>Click here</a> and enter the activation code.<br/>"
        message +="</p>"
        message+="<p>Activation Code: <b>"+activationCode+"</b></p>"
        message +="<p>"
        message+="Regards,<br/>"
        message+="Worked.com team"
        message +="</p>"
        return message

    def GetWorkHistoryVerificationEmail(self,verificationLink,verificationCode):
        message = "<p>Dear User,</p>"
        message +="<p>"
        message+="Please <a href='"+verificationLink+"'>Click here</a> and enter the verification code.<br/>"
        message +="</p>"
        message+="<p>Activation Code: <b>"+verificationCode+"</b></p>"
        message +="<p>"
        message+="Regards,<br/>"
        message+="Worked.com team"
        message +="</p>"
        return message

    def GetShareProfileEmail(self,profileLink,msg,userFullName,expiryDate):
        message = "<p>Dear User,</p>"
        message +="<p>"
        message+="Please <a href='"+profileLink+"'>Click here</a> to access profile link of "+userFullName+".<br/>"
        message+="Access to this link will be expired on "+expiryDate+".<br/>"
        message +="</p>"
        if msg!="":
            message+="<p>Message : <b>"+msg+"</b></p>"
        message +="<p>"
        message+="Regards,<br/>"
        message+=userFullName
        message +="</p>"
        return message