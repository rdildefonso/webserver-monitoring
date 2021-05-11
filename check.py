import os
from requests import get

URL = os.environ.get('HEALTHCHECK_URL', 'http://127.0.0.1:5000/healthcheck')


def send_email(subject, body):
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    SMTP_SERVER = os.environ.get('HEALTHCHECK_ALERT_SMTP_SERVER', 'localhost')
    SMTP_PORT = int(os.environ.get('HEALTHCHECK_ALERT_SMTP_PORT', 587))
    SMTP_USERNAME = os.environ.get('HEALTHCHECK_ALERT_SMTP_USERNAME', 'admin')
    SMTP_PASSWORD = os.environ.get('HEALTHCHECK_ALERT_SMTP_PASSWORD', 'admin')
    EMAIL_FROM = os.environ.get('HEALTHCHECK_ALERT_SENDER', 'admin@thisfish.co')
    EMAIL_TO = os.environ.get('HEALTHCHECK_ALERT_RECEPIENTS', 'admin@thisfish.co')
    print(f'{SMTP_SERVER}:{SMTP_PORT} - {SMTP_USERNAME} - {SMTP_PASSWORD} - {EMAIL_FROM} - {EMAIL_TO}')
    print(f'subject: {subject}\nbody: {body}')
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject
    msg.set_content(f'{body}\n\nThis is an automated alert')
    client = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    try:
        client.login(SMTP_USERNAME, SMTP_PASSWORD)
        client.send_message(msg)
    except Exception as e:
        print(f'alert error: {e}')
    else:
        print(f'email sent')
    finally:
        client.quit()


try:
    resp = get(URL)
except Exception as e:
    send_email('Application Error', e)
    exit(1)
else:
    if resp.status_code != 200:
        send_email('Application Return Not Expected', f'request to {URL} returned {resp.status_code}')
        exit(1)
    exit(0)
