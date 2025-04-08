import random
from datetime import datetime
import pandas
import smtplib
import random

my_email = 'surajkukkipady649@gmail.com'
password = 'spbrufupzqrwkdof'

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:

        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_dict[today_tuple]["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")