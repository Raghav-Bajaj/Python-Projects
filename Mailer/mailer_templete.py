from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

import smtplib, ssl

from email import encoders



with open('contacts.txt', 'r') as f:
    contacts= f.readlines()
with open('names.txt', 'r') as f:
    names = f.readlines()

for (name,contact) in zip(names,contacts):
    lower = 'This email is generated to test the mailer function part 2'
    message = ''
    port = 587
    server = "smtp.gmail.com"
    sender = <add your email here>
    password = <add your password here>
    msg = MIMEMultipart()       
    lower = 'This email is generated to test the mailer function'
    message = 'Dear ' + name + '\n' + lower
    msg.attach(MIMEText(message, "plain"))
    filename = "TestPDFfile.pdf"
    with open(filename, "rb") as pdf:
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(pdf.read())

    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    msg.attach(attachment)
    SSLcontext = ssl.create_default_context()
    with smtplib.SMTP(server,port) as smtp:
        smtp.starttls(context=SSLcontext)
        smtp.login(sender, password)
        smtp.sendmail(sender,contact, msg.as_string())
        smtp.quit()
