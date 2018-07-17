import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("sachinwadi1408@gmail.com","sachinwadi@3049")
message = "hi hello"
server.sendmail("sriharsha8811@gmail.com","sriharsha8811@gmail.com",message)
print("sss")
server.quit()
