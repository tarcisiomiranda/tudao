- https://www.linuxtechi.com/reduce-size-lvm-partition/
- https://www.systutorials.com/shrinking-a-ext4-file-system-on-lvm-in-linux/
- https://linuxtiwary.com/2017/03/06/reduce-size-of-ext3ext4-lvm-partition-in-rhel567-and-centos567-using-lvreduce-command/

## Umount
`sudo umount /srv/docker`

## e2fsck
`sudo e2fsck -f /dev/hosts/docker`

## Resize2fs (nunca menor que o total usado)
`sudo resize2fs /dev/hosts/docker 62G`

## Agora vamos usar o lvreduce
`sudo lvreduce -L 62G /dev/hosts/docker`

## e2fsck novamente
`sudo e2fsck -f /dev/hosts/docker`
