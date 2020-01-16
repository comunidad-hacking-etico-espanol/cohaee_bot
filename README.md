# Comunidad de Hacking Ético - Español
## https://t.me/HackingEticoEs

### Contribuidores: 
- Juan Arriagada ( @jarriagada - Telegram)

### Documentación:
- https://python-telegram-bot.readthedocs.io/en/stable/
- https://firebase.google.com/docs/firestore/quickstart

```console
BoT@CoHaEE:~$ git clone https://github.com/comunidad-hacking-etico-espanol/cohaee_bot.git
BoT@CoHaEE:~$ cd cohaee_bot
BoT@CoHaEE:~$ git checkout develop
BoT@CoHaEE:~$ touch .env
BoT@CoHaEE:~$ vim .env
```
```vim
# Telegram
TELEGRAM_TOKEN=

# Config
ADMIN_LIST=MisterWh1t3,jarriagada
CHAT_LIST=-1001475695377
```
```console
BoT@CoHaEE:~$ touch firebase.json
BoT@CoHaEE:~$ vim firebase.json
```
```vim
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": ""
}
```
```console
BoT@CoHaEE:~$ pip3 install -r requirements.txt
BoT@CoHaEE:~$ python3 main.py
```