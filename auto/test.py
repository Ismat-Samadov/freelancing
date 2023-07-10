import smtplib

MY_EMAIL = "ismetsemedov@gmail.com"
MY_PASSWORD = "lmjareknmmweotsp"
TO_EMAIL= "Ismat.Samadov@kapitalbank.az"
connection = smtplib.SMTP("smtp.gmail.com") # port=587
connection.starttls()
connection.login(MY_EMAIL, MY_PASSWORD)
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL,
    msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
)
