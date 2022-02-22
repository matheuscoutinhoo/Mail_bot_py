import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

try:
    fromaddr = "Your email here."
    toaddr = "Recipient's email here."
    msg = MIMEMultipart()

    msg['From'] = fromaddr 
    msg['To'] = toaddr
    msg['Subject'] = "Tittle of the email here."

    body = "\nThe body of the email here."

    msg.attach(MIMEText(body, 'plain'))

    filename = 'Attached file name here (with extension).'

    attachment = open(filename,'rb')


    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    attachment.close()

    server = smtplib.SMTP('smtp.outlook.com', 587)
    server.starttls()
    server.login(fromaddr, "Your email password here.")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print('\nEmail successfully sent.')
except:
    print("\nError while sending the email.")