import requests
import datetime
import base64
import json
import uuid
from jwcrypto import jwt, jwk

def timestamp():
    return "%s.001Z" % (datetime.datetime.utcnow().replace(microsecond=0).isoformat())

def nonce():
    random = uuid.uuid4().hex
    return base64.b32encode(random)[:26]

signing_key = jwk.JWK(**{'k': base64.b64encode("G4KuYxylN9ZYRxiFxRCQ"), 'kty':'oct'})
client_id = "OMB_CVY_AND_3A0"
#UNCOMMENT LINE BELOW AND ADD RANDOM UUIDV4 FROM https://www.uuidgenerator.net/ FOR THIS TO WORK
#device_id = "INSERT_RANDOM_UUIDV4_HERE"
username = "ONSTAR_USERNAME"
password = "ONSTAR_PASSWORD"
pin = "ONSTAR_PIN"
vin_number = "VEHICLE_VIN_NUMBER"

headers_auth = {
    'Accept': 'application/json',
    'Accept-Language': 'en',
    'Content-Type': 'text/plain',
    'Host': 'api.gm.com',
    'Connection': 'close',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'okhttp/3.9.0'
}

data_auth = {
  "client_id": client_id,
  "device_id": device_id,
  "grant_type": "password",
  "nonce": nonce(),
  "password": password,
  "scope": "onstar gmoc commerce msso",
  "timestamp": timestamp(),
  "username": username
}

token_auth = jwt.JWT(header={"alg": "HS256", "typ": "JWT"}, claims=data_auth)
token_auth.make_signed_token(signing_key)
token_auth_encoded = token_auth.serialize()
print "REQUEST_AUTH %s" % (token_auth_encoded)

response_auth = requests.post('https://api.gm.com/api/v1/oauth/token', headers=headers_auth, data=token_auth_encoded)
print "RESPONSE_AUTH %d: %s" % (response_auth.status_code, response_auth.text)

response_auth_jwt  = jwt.JWT(key=signing_key, jwt=response_auth.text)

response_auth_json = json.loads(response_auth_jwt.claims)

oauth_token = response_auth_json["access_token"]

headers_connect = {
    'Accept': 'application/json',
    'Authorization': 'Bearer %s' % (oauth_token),
    'Accept-Language': 'en',
    'Content-Type': 'application/json; charset=UTF-8',
    'Host': 'api.gm.com',
    'Connection': 'close',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'okhttp/3.9.0',
}

data_connect = '{}'

print "REQUEST_CONNECT!"

response_connect = requests.post("https://api.gm.com/api/v1/account/vehicles/%s/commands/connect" % (vin_number), headers=headers_connect, data=data_connect)
print "RESPONSE_CONNECT %d: %s" % (response_connect.status_code, response_connect.text)

headers_upgrade = {
    'Accept': 'application/json',
    'Authorization': 'Bearer %s' % (oauth_token),
    'Accept-Language': 'en',
    'Content-Type': 'text/plain',
    'Host': 'api.gm.com',
    'Connection': 'close',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'okhttp/3.9.0',
}

data_upgrade  = {
  "client_id": client_id,
  "credential": pin,
  "credential_type": "PIN",
  "device_id": device_id,
  "grant_type": "password",
  "nonce": nonce(),
  "timestamp": timestamp(),
}

token_upgrade = jwt.JWT(header={"alg": "HS256", "typ": "JWT"}, claims=data_upgrade)
token_upgrade.make_signed_token(signing_key)
token_upgrade_encoded = token_upgrade.serialize()
print "REQUEST_UPGRADE %s" % (token_upgrade_encoded)

response_upgrade = requests.post('https://api.gm.com/api/v1/oauth/token/upgrade', headers=headers_upgrade, data=token_upgrade_encoded)
print "RESPONSE_UPGRADE %d: %s" % (response_upgrade.status_code, response_upgrade.text)

headers_remotestart = headers_connect
data_remotestart = data_connect

print "REQUEST_REMOTESTART!"

response_remotestart = requests.post("https://api.gm.com/api/v1/account/vehicles/%s/commands/start" % (vin_number), headers=headers_remotestart, data=data_remotestart)
print "RESPONSE_REMOTESTART %d: %s" % (response_remotestart.status_code, response_remotestart.text)
