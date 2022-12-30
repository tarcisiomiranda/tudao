## Install YQ
```
export VERSION=v4.30.6 && \
export BINARY=yq_linux_amd64 && \
wget https://github.com/mikefarah/yq/releases/download/${VERSION}/${BINARY} -O /usr/bin/yq && \
chmod +x /usr/bin/yq
```

## Install salt 3004.2 on Ubuntu 22.04
```
curl -Ls https://bootstrap.saltstack.com | sh /dev/stdin -FXPdq stable 3004.2
```
