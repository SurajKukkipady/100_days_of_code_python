import smtplib
import datetime as dt
import random

my_email = 'surajkukkipady649@gmail.com'
password = 'spbrufupzqrwkdof'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:  # Monday
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='suraj.kukkipady1@gmail.com',
                            msg=f'Subject:Monday Motivation\n\n{quote}')
