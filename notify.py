import smtplib

senderEmail = "accesscontrolnotify@gmail.com" #Replace with other email to be associated with the system
receiverEmail = "ahkubwayo@gmail.com" #Replace it with your email to receive notification sent by the system

password = "reum jabo tecy tfbe" #App password for the email associated with the system
subject = 'Access Control Notification'
message = "Attempt to gain access through the door!"
header='To: ' + receiverEmail + '\n' + 'From: ' + senderEmail + '\n' + 'Subject: ' + subject

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, password)
print("Login successful!")
server.sendmail(senderEmail, receiverEmail, header + '\n\n'+ message)
print("Email has been sent to ", receiverEmail)





