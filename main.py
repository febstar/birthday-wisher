import smtplib
import datetime as dt
import random
import pandas

my_email = "febstarowen@gmail.com"
password = "gsgbgbeqxnwlvibq"


to_send = pandas.read_csv("birthdays.csv")
to_send = to_send.to_dict()
for i in range(len(to_send['name'])):
    name = to_send['name'][i]
    mail = to_send['email'][i]
    year = to_send['year'][i]
    month = to_send['month'][i]
    day = to_send['day'][i]
    b_day = dt.datetime.now()
    b_month = b_day.month
    d_day = b_day.day
    if month == b_month and day == d_day:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
            final_letter = letter.replace("[NAME]", name)
            with open(f"letter_templates/birthday for {name}.txt",mode="w") as complete:
                complete.write(final_letter)
            with open(f"letter_templates/birthday for {name}.txt",mode="r") as files:
                to_deliver = files.read()
            with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=mail,
                                    msg=f"Subject:Happy Birthday\n\n{to_deliver}")