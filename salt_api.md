[Doc Salt API](https://docs.saltproject.io/en/latest/ref/netapi/all/salt.netapi.rest_cherrypy.html)
```
salt-call --local tls.create_self_signed_cert
```

### api.conf
***/etc/salt/master.d/api.conf***
```
rest_cherrypy:
  port: 8000
  ssl_crt: /etc/pki/tls/certs/localhost.crt
  ssl_key: /etc/pki/tls/certs/localhost.key

netapi_enable_clients:
  - local

external_auth:
  pam:
    salt_python:
      - '*':
        - .*

```

### 
```
curl -sSk https://192.168.29.40:8000/login \
    -H 'Accept: application/x-yaml' \
    -d username=salt_python \
    -d password=vasco \
    -d eauth=pam

curl -sSk https://192.168.29.40:8000 \
    -H "Accept: application/x-yaml" \
    -H "X-Auth-Token: vasco_da_gama" \
    -d client='local' \
    -d tgt='*' \
    -d fun='test.ping'
```
