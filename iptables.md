## NAT SSH
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 8001 -j REDIRECT --to-port 22
```
