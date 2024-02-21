import random
import sys
# import os



def sendMail(result, email, sender_email, password):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Create message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email

    message['Subject'] = 'OTP from secure-otp-service'

    # Craft the HTML email body
    body = """\
    <html>
        <body>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNfBuPO5zmKvQMyV8n6sk2KyIRXL_E8V2hUw&usqp=CAU" width="100px"></img>
            <br></br>
            <p>Dear User,</p>
            <p>Thank you for using our secure OTP service. Your one-time password (OTP) is: <span style="font-size: 30px; color: #FF5733;">{}</span></p>
            <p>This OTP is required to access certain features or complete a transaction securely.</p>
            <p>If you did not request this OTP or have any concerns, please contact our support team <a> uppinurigouthamreddy@gmail.com </a>immediately.</p>
            <p>Best regards,<br>Your Secure OTP Service Team</p>
        </body>
    </html>
    """.format(result)

    message.attach(MIMEText(body, 'html'))

    # Establish SMTP connection
    errorsInPythonScript = []
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to the server
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        errorsInPythonScript.append(str(e))
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