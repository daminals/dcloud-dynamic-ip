import smtplib, os
from dotenv import load_dotenv

load_dotenv()

user = os.environ.get('user', 3)
password = os.environ.get('password', 3)
to = os.environ.get('to', 3)
subject = 'Dynamic IP Change'

with open('ip.txt', 'r') as ip_file:
    init_ip = ip_file.read()

with open('new_ip.txt', 'r') as new_ip_file:
    new_ip = new_ip_file.read()

body=f"Old IP: {init_ip}; New IP: {new_ip}"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (user, to, subject, new_ip)

if new_ip != init_ip:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(user, password)
    smtp_server.sendmail(user, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")