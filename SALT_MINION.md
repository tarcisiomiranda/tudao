## Gerar Token API
```
curl -sSk https://192.168.29.40:8000/login \
-H 'Accept: application/x-yaml' \
-d username='salt_python' \
-d password='' \
-d eauth='pam'
```

## Remover cahves que nao pingam
```
salt-run manage.down removekeys=True
```

## Limpar cache e regerar
```
salt-call saltutil.clear_cache
salt-call saltutil.clear_job_cache
salt-call saltutil.kill_all_jobs
salt-call saltutil.regen_keys
```

[Remover Chaves Down]('https://docs.saltproject.io/en/latest/ref/runners/all/salt.runners.manage.html#salt.runners.manage.down')
