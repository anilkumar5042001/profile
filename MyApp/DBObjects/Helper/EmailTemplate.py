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