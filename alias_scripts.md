## Print pretty using dockerps and show partitions
```
echo $'\n # Docker alias and Display Filesystem' >> ~/.bashrc && \
echo "alias dockerps='sudo docker ps --format \"table {{.Names}}\t{{.State}}\t{{.Ports}}\"'" >> ~/.bashrc && \
echo "alias dockerpc='sudo docker ps --format \"table {{.Names}}\t{{.Ports}}\"'" >> ~/.bashrc && \
echo "alias dockercc='sudo docker ps --format \"table {{.Names}}\t{{.State}}\"'" >> ~/.bashrc && \
echo "alias dockerip='sudo docker inspect -f \"{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}\"'" >> ~/.bashrc && \
echo "alias dockerss='sudo docker ps --format \"table {{.Names}}\t{{.CreatedAt}}\t{{.RunningFor}}\t{{.Size}}\"'" >> ~/.bashrc && \
echo "alias dff='df -TPh|egrep -v \"overlay|loop|shm|tmpfs\"'" >> ~/.bashrc && bash
```

## OR ONLY COMMAND USING EOL
```
cat <<EOF >> ~/.bashrc
# Formats for docker
alias dockerps='sudo docker ps --format "table {{.Names}}\t{{.State}}\t{{.Ports}}"'
alias dockerpc='sudo docker ps --format "table {{.Names}}\t{{.Ports}}"'
alias dockercc='sudo docker ps --format "table {{.Names}}\t{{.State}}"'
alias dockerip='sudo docker inspect -f "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}"'
alias dockerss='sudo docker ps --format "table {{.Names}}\t{{.CreatedAt}}\t{{.RunningFor}}\t{{.Size}}"'

# Show pretty partitions
alias dff='df -TPh|egrep -v "overlay|loop"'

# Git show branch
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
export PS1="\u@\h \[\e[32m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "

EOF
```

# exclude commnet caracteres
```
cat /etc/sudoers.d/* /etc/sudoers | egrep -v '(#|//|^[[:space:]]*$)'
```

<hr/>

# Script for show ip login screen
***Start***
## Create script
```
echo -n $'\n' | cat - /etc/issue > /tmp/issue.tmp
mv /etc/issue /etc/issue.bkp && \
mv /tmp/issue.tmp /etc/issue && \
mkdir -p /opt/meuip/ && \
touch /opt/meuip/look.sh && \
chmod u+x /opt/meuip/look.sh && \
cat <<EOF >> /opt/meuip/look.sh
#!/bin/sh
meuip=\`ifconfig enp0s3 | awk '/inet /{print \$2}' | cut -f2 -d':'\`
sed -i "1s/.*/\$meuip/" /etc/issue
EOF
```

## Create service
```
cat <<EOF >> /etc/systemd/system/meuip.service
[Unit]
After=network-online.target
Description=Run script at startup after network becomes reachable and set ip home screen

[Service]
Type=simple
RemainAfterExit=yes
ExecStart=/opt/meuip/look.sh
TimeoutStartSec=0

[Install]
WantedBy=default.target
EOF

## Enable service
```
systemctl daemon-reload && \
systemctl enable meuip && \
systemctl status meuip
```
