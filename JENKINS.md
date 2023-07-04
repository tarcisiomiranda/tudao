# Comandos comuns

## Listar plugins instalados no Jenkins
```
curl -k -X GET "https://devops.tarcisio.me/jenkins/pluginManager/api/json?depth=1" | jq '.plugins[].shortName'
```
## Como exportar jobs do jenkins
```
https://devops.tarcisio.me/jenkins/view/Saltstack/job/saltstack/job/inventory_windows_patch/config.xml
```
