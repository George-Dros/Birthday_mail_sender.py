import smtplib
import datetime as dt
import random
import pandas


my_email = "your_email"
password = "your App-password, NOT user password!"

#Update the birthdays.csv

data = pandas.read_csv("birthdays.csv")
birthdays_list = data.to_dict(orient="records")

today = dt.date.today()
month = today.month
day = today.day

#Check if today matches a birthday in the birthdays.csv and create  letter

for entry in birthdays_list:
    if entry["month"] == month and entry["day"] == day:
        birthday = entry
        num = random.randint(1,3)
        with open(f"letter_templates/letter_{num}.txt","r") as letter_in:
            letter_out = open("to_send.txt","w")
            for line in letter_in:
                letter_out.write(line.replace("[NAME]",f"{birthday['name']}"))
            letter_out.close()
            with open("to_send.txt", "r") as letter_out:
                to_send = letter_out.read()


#Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email, to_addrs=f"{birthday['email']}",
                                    msg=f"Subject:Happy Birth-day!\n\n{to_send}")
    connection.close()