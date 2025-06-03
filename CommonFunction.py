import json
import datetime
from six import string_types
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from TblGatePassCustomRepository import *
# from tblGatePassMaterialDetailsRepository import *
# from mstVendorRepository import *
from flask import Flask, render_template, Response, jsonify, request
from email.header import Header
from email.utils import parseaddr, formataddr
import traceback


def to_json(obj, id):
    cls = type(obj)
    d = dict((c, getattr(obj, c)) for c in vars(cls) if isinstance(getattr(cls, c), property))
    d["id"] = id

    # print(d)
    return d


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def datetime_decoder(d):
    if isinstance(d, list):
        pairs = enumerate(d)
    elif isinstance(d, dict):
        pairs = d.items()
    result = []
    for k, v in pairs:
        if isinstance(v, string_types):
            try:
                # The %f format code is only supported in Python >= 2.6.
                # For Python <= 2.5 strip off microseconds
                # v = datetime.datetime.strptime(v.rsplit('.', 1)[0],
                #     '%Y-%m-%dT%H:%M:%S')
                v = datetime.datetime.strptime(v, '%d-%m-%Y %H:%M:%S')
            except ValueError:
                try:
                    v = datetime.datetime.strptime(v, '%d-%m-%Y %H:%M:%S').date()
                except ValueError:
                    pass
        elif isinstance(v, (dict, list)):
            v = datetime_decoder(v)
        result.append((k, v))
    if isinstance(d, list):
        return [x[1] for x in result]
    elif isinstance(d, dict):
        return dict(result)


def SendAuthMail(Mailbody, reciver):
    subject = "New GatePass Aproval Request"
    body = Mailbody
    sender_email = "sourcetechpune@gmail.com"
    receiver_email = reciver
    password = "Enter password"
    print("In Common Function")
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails
    # Add body to email
    message.attach(MIMEText(body, "html"))
    filename = "outputs/emailcompose.html"  # In same directory as script
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    try:

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            # with smtplib.SMTP_SSL("smtprelay.hoganas.int", 25, context=context) as server:
            # server.login("inaudi", 'password')
            server.sendmail(sender_email, receiver_email, text)
    except:
        return False
    return True


def SendHTMLMail(Mailbody, reciver):
    username = "INITPUNE@hoganas.com"
    password = "Hipl@2022$"
    host = "smtprelay.hoganas.int"
    port = "25"
    sender = "donotreply@hoganas.com"
    secure = "try"
    # username = "sourcetechpune@gmail.com"
    # password = "Enter password"
    # host = "smtp.gmail.com"
    # port = "465"
    # sender = "sourcetechpune@gmail.com"
    # secure = "true"  # "try"
    recipients = reciver
    subject = "New Gatepass for approval"
    body = Mailbody
    charset = "UTF8"
    timeout = 10
    code = 0
    secure_state = False

    sender_phrase, sender_addr = parseaddr(sender)
    smtp = None
    if not body:
        body = subject

    # if secure == "true":
    #     try:
    #         msg = MIMEMultipart(_charset=charset)
    #         msg['From'] = formataddr((sender_phrase, sender_addr))
    #         msg['Subject'] = Header(subject, charset)
    #         msg.preamble = "Multipart message"
    #         part = MIMEText(body, "html")
    #         msg.attach(part)
    #         composed = msg.as_string()
    #
    #         context = ssl.create_default_context()
    #         with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    #             smtp.login(sender, password)
    #             # with smtplib.SMTP_SSL("smtprelay.hoganas.int", 25, context=context) as server:
    #             # server.login("inaudi", 'password')
    #             result = smtp.sendmail(sender_addr, recipients, composed)
    #             print(result)
    #         smtp.quit()
    #     except:
    #         return False
    #     return True

    if secure != 'never':
        smtp = smtplib.SMTP_SSL(timeout=timeout)
        #   code, smtpmessage = smtp.connect(host, port)
        #  secure_state = True
        # ssl.SSLError: [SSL: UNKNOWN_PROTOCOL] unknown protocol (_ssl.c:579)

    if not secure_state:
        smtp = smtplib.SMTP(timeout=timeout)
        code, smtpmessage = smtp.connect(host, port=port)

        # this was always false....
    print(smtp.has_extn('STARTTLS'))
    print(code)

    if int(code) < 0:
        if not secure_state and secure in ('starttls', 'try'):
            # if smtp.has_extn('STARTTLS'):

            smtp.starttls()
            secure_state = True

        # else:
        #   if secure == 'starttls':
        #     print 'StartTLS is not offered on server'

        smtp.ehlo()

    if username and password:
        if smtp.has_extn('AUTH'):
            # try:
            smtp.login(username, password)
        # except smtplib.SMTPAuthenticationError:
        #    module.fail_json(rc=1, msg='Authentication to %s:%s failed, please check your username and/or password' % (host, port))
        # except smtplib.SMTPException:
        #    module.fail_json(rc=1, msg='No Suitable authentication method was found on %s:%s' % (host, port))
        else:
            print("No Authentication on the server at")

    if not secure_state and (username and password):
        print('Username and Password was sent without encryption')
    msg = MIMEMultipart(_charset=charset)
    msg['From'] = formataddr((sender_phrase, sender_addr))
    msg['Subject'] = Header(subject, charset)
    msg.preamble = "Multipart message"
    part = MIMEText(body, "html")
    msg.attach(part)
    composed = msg.as_string()
    result = smtp.sendmail(sender_addr, recipients, composed)
    print(result)
    smtp.quit()
