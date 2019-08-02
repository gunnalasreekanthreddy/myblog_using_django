# skipped your comments for readability
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(tomail,otp):
        me = "noreplay.myblog653@gmail.com"
        my_password = "Apalya@01"
        you = tomail

        msg = MIMEMultipart()
        msg['Subject'] = "otp has sent to u"
        msg['From'] = me
        msg['To'] = tomail

        html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
        message = "your otp is" + otp
        part2 = MIMEText(html, 'html')
        msg.attach(MIMEText(message))
        msg.attach(part2)

        # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
        s = smtplib.SMTP_SSL('smtp.gmail.com')
        # uncomment if interested in the actual smtp conversation
        # s.set_debuglevel(1)
        # do the smtp auth; sends ehlo if it hasn't been sent already
        s.login(me, my_password)

        s.sendmail(me, you, msg.as_string())
        s.quit()
