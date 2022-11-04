## Remove CLOUD-INIT, LXD and SNAPD
```
sudo snap remove --purge lxd \
&& sudo snap remove --purge core20 \
&& sudo snap remove --purge snapd \
&& sudo apt --purge autoremove snapd \
&& sudo touch /etc/cloud/cloud-init.disabled \
&& sudo dpkg-reconfigure cloud-init \
&& sudo apt --purge autoremove cloud-init \
&& sudo rm -rf /etc/cloud/ \
&& sudo rm -rf /var/lib/cloud/
```
