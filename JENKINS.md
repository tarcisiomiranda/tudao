# CoMO LISTAR OS PLUGINS INTALADOS
```
curl -k -X GET "https://devops.tarcisio.me/jenkins/pluginManager/api/json?depth=1" | jq '.plugins[].shortName'
```
