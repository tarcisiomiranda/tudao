# How to disable systemd-resolved in Ubuntu

## Stages

- Disable and stop the systemd-resolved service:

		sudo systemctl disable systemd-resolved.service
		sudo systemctl stop systemd-resolved

- Then put the following line in the `[main]` section of your `/etc/NetworkManager/NetworkManager.conf`:

		dns=default

- Delete the symlink `/etc/resolv.conf`

		rm /etc/resolv.conf

- Restart network-manager

		sudo service network-manager restart

## Sources
- https://askubuntu.com/questions/907246/how-to-disable-systemd-resolved-in-ubuntu
- https://yenthanh.medium.com/some-simple-things-for-tuning-your-ubuntu-server-3db99383eadb


## Revert
```
ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
systemctl restart systemd-resolved
systemctl enable systemd-resolved
```
