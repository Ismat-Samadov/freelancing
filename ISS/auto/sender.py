import smtplib
import time
import os

MY_EMAIL = "ismetsemedov@gmail.com"
MY_PASSWORD = "lmjareknmmweotsp"
TO_EMAIL= "ismetsemedli@mail.ru"

while True:
    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        msg = "Subject: Look Up\nTo: {}\nFrom: {}\n\nThe ISS is above you in the sky.".format(TO_EMAIL, MY_EMAIL)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=msg
        )

        connection.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

    time.sleep(2)
