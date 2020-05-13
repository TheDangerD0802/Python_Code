#!/usr/bin/python36

import cv2

cap = cv2.VideoCapture(0)
ret , frame = cap.read()
cv2.imwrite('/root/cam.png', frame)
cap.release()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




msg = MIMEMultipart()

msg['From'] = "winterinternshiplinuxworld@gmail.com"

msg['To'] = "vdaga@lwindia.com"

msg['Subject'] = "my image"

body = "this is mail with body"


msg.attach(MIMEText(body, 'plain'))

filename = 'cam.png'

attachment = open('/root/cam.png', 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename={}".format(filename))
msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com' , 587)
s.starttls()
s.login("winterinternshiplinuxworld@gmail.com", "mypass")
text=msg.as_string()
s.sendmail('winterinternshiplinuxworld@gmail.com', 'vdaga@lwindia.com', text)
s.quit()

