#!/usr/bin/python3

'''
# Gen SSL + Godady
https://github.com/miigotu/certbot-dns-godaddy

# Install libs
pip3 install cryptography

# How to use:
python3 check_ssl.py -i /etc/letsencrypt/live/upixels.com.br/fullchain.pem

# Create alias linux
cp -a check_ssl.py /usr/local/bin/check_ssl \
&& chmod +x /usr/local/bin/check_ssl

# /etc/crontab
0 6 * * * root /usr/local/bin/check_ssl >> /var/log/renew_cert.log 2>&1
'''

from cryptography import x509
from cryptography.hazmat.backends import default_backend
import subprocess
import requests
import datetime
import argparse


def send_telegram(cert, msg):
    url = 'https://api.telegram.org/'
    BOT_ID = ''
    CHT_ID = ''
    DT_MSG = '''\
Cert: {}
Days: {}
'''.format(cert, msg)

    try:
        if CHT_ID is None or BOT_ID is None:
            raise Exception({
                'status': 500,
                'message': 'Error when send message',
                'MSG': DT_MSG
            })

        else:
            params = (
                ('chat_id', CHT_ID),
                ('text', DT_MSG),
                ('parse_mode', 'HTML')
            )

            new_url = '{}{}/sendmessage'.format(url, BOT_ID)
            res = requests.get(new_url, params=params)

            if res.status_code == 200:
                return {
                    'status': 200,
                    'message': 'message sent',
                    'MSG': DT_MSG
                }

    except Exception as err:
        return {
            'status': 500,
            'message': 'Error when send message - {}'.format(err),
            'MSG': DT_MSG
        }

def renew_cert():
        cmmd = '''certbot certonly \
    --authenticator dns-godaddy \
    --dns-godaddy-credentials ~/credentials.ini \
    --dns-godaddy-propagation-seconds 900 \
    --agree-tos \
    --email email@email.com \
    --keep-until-expiring --non-interactive --expand \
    --server https://acme-v02.api.letsencrypt.org/directory \
    -d 'domain.com.br' \
    -d '*.domain.com.br'
'''
        proc = subprocess.Popen(cmmd, stdout=subprocess.PIPE, shell=True, \
        stderr=subprocess.PIPE, universal_newlines=True)
        out, err = proc.communicate()

        if 'successfully received certificate' in out.lower():
            print('successfully certificate renew')
        else:
            print('successfully certificate failed')

def check_file(_file=None):
    if _file is not None:
        file = _file
    else:
        file = "/etc/letsencrypt/live/domain.com.br/fullchain.pem"
    with open(file, 'rb') as f:
        data = f.read()
        f.close

    cert = x509.load_pem_x509_certificate(data, default_backend())
    expiry_date = cert.not_valid_after.date()
    d_remaining = expiry_date - datetime.date.today()

    if d_remaining.days <= 10:
        print('cert {} will expire in {} days'.format(file, d_remaining.days))
    elif d_remaining.days <= 5:
        send_telegram(file, d_remaining.days)
        print('call renew certificate await ...')
        renew_cert()
    else:
        print('cert {} valid {} day(s)'.format(file, d_remaining.days))


# Arguments
parser = argparse.ArgumentParser(description='Run to check ssl file')
parser.add_argument('-i','--file', type=str,
                    help='Identify file to check ssl')

args = parser.parse_args()
if args.file:
    check_file(args.file)
else:
    check_file()
