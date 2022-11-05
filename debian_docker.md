# Remove old containers
```
apt-get remove docker docker-engine docker.io containerd runc
```
***Install packages***
```
sudo apt-get update \
&& sudo apt-get install ca-certificates curl gnupg lsb-release sudo -y

sudo mkdir -p /etc/apt/keyrings \
&& curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && sudo apt update
```

### install docker without compose plugin (#recommend)
***Docker and compose binari***
```
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo curl -L "https://github.com/docker/compose/releases/download/v2.11.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
sudo chmod +x /usr/local/bin/docker-compose
```

***OR Docker and compose plugin***
### isntall docker with compose plugin
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
## Enable start-up docker and set group docker for your user
```
sudo systemctl enable docker && sudo usermod -aG docker $USER
```
