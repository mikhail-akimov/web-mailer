from flask_mail import Message
from app import mail


def send_email(subject, sender, recipients, cc, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc)
    msg.body = text_body
    msg.html = text_body.replace('\r\n', '<br>')
    mail.send(msg)
    return True