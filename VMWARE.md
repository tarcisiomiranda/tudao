# update vmware with .zip ex: 6.7 to 7.0
***Enter maintenance mode***
```
esxcli system maintenanceMode set --enable true
```

***Apply update to change major version***
```
esxcli software vib update --depot /vmfs/volumes/datastore1/patch_update/update.zip
```

***Apply patch the same version***
```
esxcli software vib install --depot /vmfs/volumes/datastore1/patch_update/update.zip
```
