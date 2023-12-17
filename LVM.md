# Reduce LV
```
umount /dev/harbor-vg/home
```

```
e2fsck -f /dev/harbor-vg/home
```

```
resize2fs /dev/harbor-vg/home [NOVO_TAMANHO]G
```

```
lvreduce -L [NOVO_TAMANHO]G /dev/harbor-vg/home
```

```
e2fsck -f /dev/harbor-vg/home
```

```
mount /dev/harbor-vg/home
```
