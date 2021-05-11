from requests import get

URL = 'http://127.0.0.1:5000/error'


def send_email(subject, body):
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
