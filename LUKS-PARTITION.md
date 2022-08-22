# Open LUKS partition

## First
```
sudo apt-get install cryptsetup
```
### To decrypt the volume:

```
sudo cryptsetup luksOpen /dev/sda1 luks_1
sudo mount /dev/mapper/luks_1 /mnt/storage4/
```
### Now you can mount it as usual:
```
sudo mkdir /media/luks_1
sudo mount /dev/mapper/luks_1 /media/luks_1
```
### To lock the container again, it needs to be unmounted first:

```
sudo umount /media/luks_1
sudo cryptsetup luksClose luks_1
```
### To automatically put it in the /media location, use the udisks tool

```
sudo udisks --mount /dev/mapper/luks_1
```
