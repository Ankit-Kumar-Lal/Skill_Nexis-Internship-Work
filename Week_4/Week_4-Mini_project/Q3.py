# 3. Automate Email Sending Using smtplib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass


# Function to send email
def send_email():

    sender_email = input("Enter your Gmail address: ")
    sender_password = getpass("Enter your Gmail App Password: ")

    receiver_email = input("Enter receiver's email address: ")

    subject = input("Enter email subject: ")
    message = input("Enter your email message: ")

    # Create email message
    email = MIMEMultipart()

    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject

    email.attach(MIMEText(message, "plain"))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)

        # Start secure connection
        server.starttls()

        # Login to sender's Gmail account
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(
            sender_email,
            receiver_email,
            email.as_string()
        )

        print("\nEmail sent successfully!")

    except Exception as e:
        print("\nFailed to send email.")
        print("Error:", e)

    finally:
        if "server" in locals():
            server.quit()


# Main program
print("===== EMAIL AUTOMATION SYSTEM =====")

send_email()


