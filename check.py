import os
from requests import get

URL = os.environ.get('HEALTHCHECK_URL', 'http://127.0.0.1:5000')


def send_email(subject, body):
    import smtplib
    server = smtplib.SMTP(os.environ.get('HEALTHCHECK_ALERT_SMTP', 'localhost'))
    server.sendmail(os.environ.get('HEALTHCHECK_ALERT_SENDER', 'admin@thisfish.co'), os.environ.get('HEALTHCHECK_ALERT_RECEPIENTS', 'app_support@thisfish.co'))
    print(f'subject: {subject}\nbody: {body}')


try:
    resp = get(URL)
except Exception as e:
    send_email('app error', e)
    exit(1)
else:
    if resp.status_code != 200:
        send_email('wrong code', f'request to {URL} returned {resp.status_code}')
        exit(1)
    exit(0)
