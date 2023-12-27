```
sudo tcpdump -i ens160 'port 443 and net 200.222.222.0/24'
sudo tcpdump -i ens160 'port 443 and host 200.222.222.170'
sudo tcpdump -i ens160 'port 443'
```
