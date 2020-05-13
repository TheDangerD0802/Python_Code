#!/usr/bin/python36

import cv2

cap  =  cv2.VideoCapture(0)

ret, photo  = cap.read()

cv2.imwrite('/root/cam.png', photo)
cap.release()


import smtplib
session = smtplib.SMTP("smtp.gmail.com" , 587)
session.starttls()
session.login("winterinternshiplinuxworld@gmail.com", "$kavyalw@123")
session.sendmail("winterinternshiplinuxworld@gmail.com" , "vdaga@lwindia.com", "somebody try to hack ur system using USB")

session.quit()






