## Status

```
apk add chrony
rc-service chronyd start
rc-update add chronyd default
```

```
chronyc tracking
```

```
ntpctl -s status
```

### Force sync
```
chronyc -a makestep
```

```
rc-service chronyd restart
```
