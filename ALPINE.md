## ADD crond
```
apk add --update busybox
touch /var/spool/cron/crontabs/root
chmod 600 /var/spool/cron/crontabs/root

rc-update add crond default
/etc/init.d/crond start

***/var/spool/cron/crontabs/root***
# Backup blog
01      1       *       *       *     "/usr/bin/python3 /srv/blog/backup.py --all --prod

crontab -e e listar as tarefas cron ativas usando o comando crontab -l.
Certifique-se de editar o arquivo cron como usuário root.
```
