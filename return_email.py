"""
This is a python script for sending back condirmation to the user after submission.
Author: Abdus Sattar Mia
"""
from email.mime.text import MIMEText
import smtplib

def sendEmail(name, email):
    from_email="courseloops@gmail.com"
    from_password="Your gmail password here"
    to_email=email

    subject="CourseLoops sign up confirmation"
    message ="Hey there, \n\n This email confirms your sign up to the courseloops. \n Thanks for your sign up to the courseloops."

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To']=to_email
    msg['From'] =from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
