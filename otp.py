import random
import sys
# import os



def sendMail(result,email,sender_email,password):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # from dotenv import load_dotenv,dotenv_values
    # load_dotenv()


    # sender_email = str(os.getenv("SENDER_MAIL"))
    receiver_email = email[6:len(email)]
    # password = str(os.getenv("SENDER_KEY"))

    # Create message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email

    message['Subject'] = 'OTP from secure-otp-service\n'

    # Email content
    body = str(result)
    message.attach(MIMEText(body, 'plain'))

    # Establish SMTP connection
    errorsInPythonScript=[]
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to the server
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        #print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        errorsInPythonScript.append(str(e))
        errorsInPythonScript.append("environment variables : ")
        errorsInPythonScript.append(sender_email)
        errorsInPythonScript.append(password)
        print(e)
    finally:
        # Close the SMTP server connection
        server.quit()
    return errorsInPythonScript


def generate_otp(email,sender_email,password):
    result = random.randint(100000,999999)
    print(result)
    l=[]
    l.append(result)

    l.append(sendMail(result,email,sender_email,password))
    return(l)

email=sys.argv[1]
sender_email = sys.argv[2]
password = str(sys.argv[3]+sys.argv[4]+sys.argv[5]+sys.argv[6])
#print(sender_email)
#print(password)
generate_otp(email,sender_email,password)