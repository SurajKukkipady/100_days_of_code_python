import smtplib

my_email = 'surajkukkipady649@gmail.com'
password = 'spbrufupzqrwkdof'

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs='suraj.kukkipady1@gmail.com', msg='Hello')
connection.close()


