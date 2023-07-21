# update docker-compose Linux AMD_64
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
sudo chmod +x /usr/local/bin/docker-compose && \
docker-compose --version
```


# create subnet for docker
```
docker network create --attachable --driver bridge --ipam-driver default --subnet 192.168.255.0/24 ce_frontend
```
