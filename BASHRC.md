## OR ONLY COMMAND USING EOL
```
cat <<EOF > ~/.bashrc
# .bashrc

# User specific aliases and functions
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Docker Formats
alias dockerps='sudo docker ps --format "table {{.Names}}\t{{.State}}\t{{.Ports}}"'
alias dockerpc='sudo docker ps --format "table {{.Names}}\t{{.Ports}}"'
alias dockercc='sudo docker ps --format "table {{.Names}}\t{{.State}}"'
alias dockerip='sudo docker inspect -f "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}"'
alias dockerss='sudo docker ps --format "table {{.Names}}\t{{.CreatedAt}}\t{{.RunningFor}}\t{{.Size}}"'
alias dockera='sudo docker ps -a --format "table {{.Names}}\t{{.CreatedAt}}\t{{.Status}}\t{{.RunningFor}}\t{{.Size}}"'

# Saltstack
alias sall='docker exec -it saltstack bash'
alias salk='docker exec -it saltstack salt-key'
alias del='docker exec -it saltstack salt-key -y -d '
alias acc='docker exec -it saltstack salt-key -y -a '

# Pretty Partitions
alias dff='df -TPh | egrep -v "overlay|loop|shm|tmpfs|devtmpfs"'
alias dffi='df -TPhi | egrep -v "overlay|loop|shm|tmpfs|devtmpfs"'
alias lsblk='lsblk | egrep -v "loop[0-9]{1,2}"'

# Git Tools
alias git.email='git config --local user.email'
alias git.name='git config --local user.name'

# Group Containers
docker_ps_grouped () {
    docker ps --format '{{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Labels}}' | awk -F "\t" '
    BEGIN {
      print "CONTAINER ID\tNAMES\tIMAGE\tSTATUS\tPORTS\tPROFILE";
      no_profile_group = ""; # String to hold containers without a profile
    }

    {
      # Initialize the variable to hold the profile label value
      profile_found = 0;

      # Split the labels field using commas as delimiters
      n = split($6, a, ",");
      for (i = 1; i <= n; i++) {
        # Split each label into key-value pairs using '=' as delimiter
        split(a[i], kv, "=");
        if (kv[1] == "com.docker.compose.project") {
          profile = kv[2];
          profile_found = 1;
          break;
        }
      }

      # Group the output by the 'com.docker.compose.project' label or set to 'no_profile'
      if (profile_found) {
        grouped[profile] = grouped[profile] $1 "\t" $2 "\t" $3 "\t" $4 "\t" $5 "\n";
      } else {
        no_profile_group = no_profile_group $1 "\t" $2 "\t" $3 "\t" $4 "\t" $5 "\n";
      }
    }

    END {
      for (p in grouped) {
        if (p != "") {
          print "---- " p " ----";
          print "CONTAINER ID\tNAMES\tIMAGE\tSTATUS\tPORTS";
          print grouped[p];
        }
      }
      if (no_profile_group != "") {
        print "---- no_profile ----";
        print "CONTAINER ID\tNAMES\tIMAGE\tSTATUS\tPORTS";
        print no_profile_group;
      }
    }
  '
}

alias dks=docker_ps_grouped

git_branch_prompt() {
  if git rev-parse --git-dir > /dev/null 2>&1; then
    echo -n "[$(git branch --show-current)] "
  fi
}

get_cid() {
  local cid=$(grep "cmdb" /srv/xtk/config/install.ini | cut -d '=' -f2 | tr -d ' ')
  if [[ -z "$cid" ]]; then
    echo "N/A"
  else
    echo $cid
  fi
}


export PS1="[\u]@\[\e[34m\][$(get_cid)]\[\e[0m\][\h] \[\e[32m\]\w \[\e[91m\]\$(git_branch_prompt)\[\e[00m\]$ "

EOF
```

# exclude commnet caracteres
```
cat /etc/sudoers.d/* /etc/sudoers | egrep -v '(;|#|//|^[[:space:]]*$)'
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
```

## Enable service
```
systemctl daemon-reload && \
systemctl enable meuip && \
systemctl status meuip
```

## install Buildx
```
wget https://github.com/docker/buildx/releases/download/v0.12.0/buildx-v0.12.0.linux-amd64
mkdir  ~/.docker/cli-plugins/
chmod a+x buildx-v0.12.0.linux-amd64
cp buildx-v0.12.0.linux-amd64 ~/.docker/cli-plugins/docker-buildx
docker buildx version
```

## Buid with progess plain text
```
docker buildx build --progress=plain -f ./docker/svelte/Dockerfile -t tarcisiome/svelte:latest .
```

## ADD minha key
```
mkdir -p ~/.ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC/NzJRrc7OXFmHoqghOVOvxb5HyTNt4uSQ95N+BlTm+zLQMBm3VTPhxMR18bZJBWwEo5ecNEJisCiAIWf25R9i4vTJCFie8zk3IL3b5qbHMfgW8pAjoy8NiQLWzXhnXQsbX587uBi9H++p0POUqxNuJVO0Qd2r6ZSmbA8l1jrjDPAB+ER89wFFNKQ9QsNdktB94/3XP04kQlqCb9Gb6jhDaN1irznmtl7M4lrlz/DLfzORKTIOrEVRuc6YGtJyzJPEtERwFIXYuDmpxKuWFuDABenRQaiOIEz98AUk1XH3at0X11Ad1H+OJFmlJAXuD/q1hD/Y9m99HDfGk6Jj7jXt" >> ~/.ssh/authorized_keys

chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```
