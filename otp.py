import random
import sys
import os



def sendMail(result,email):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    from dotenv import load_dotenv,dotenv_values
    load_dotenv()


    sender_email = str(os.getenv("SENDER_MAIL"))
    receiver_email = email[6:len(email)]
    password = str(os.getenv("SENDER_KEY"))

    # Create message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email

    message['Subject'] = 'OTP from secure-otp-service\n'

    # Email content
    body = str(result)
    message.attach(MIMEText(body, 'plain'))

    # Establish SMTP connection
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to the server
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        print(e)
    finally:
        # Close the SMTP server connection
        server.quit()


def generate_otp(email):
    result = random.randint(100000,999999)
    print(result)

    sendMail(result,email)
    return(result)

email=sys.argv[1]
generate_otp(email)