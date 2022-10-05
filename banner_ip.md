#!/bin/sh
meuip=`ifconfig enp0s3 | awk '/inet /{print $2}' | cut -f2 -d':'`
sed -i "1s/.*/$meuip/" /etc/issue
