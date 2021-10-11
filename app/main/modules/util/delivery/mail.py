import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, COMMASPACE
from app.main.config.env_config import OUTLOOK_USER, OUTLOOK_PASSWORD
from app.main.modules.util.logger import log_send_mail


def send_mail(send_from: str, send_to: list, subject: str, text: str = None, html: str = None, files=None):
    """
            mail 전송
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    if text is not None:
        msg.attach(MIMEText(text, 'plain'))
    if html is not None:
        msg.attach(MIMEText(html, 'html'))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP('smtp.office365.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(OUTLOOK_USER, OUTLOOK_PASSWORD)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
    # log_send_mail(send_from, send_to, subject, text, html, files)
