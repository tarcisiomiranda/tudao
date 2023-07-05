# Verificar o arquivo de log e o tamanha
## Listar
```
docker inspect traefik | grep -i logpath | awk -F':' '{print $2}' | tr -d '[:space:]' | sed 's/["\,]/\n/g'
```
## Tamanho
```
docker inspect traefik | grep -i logpath | awk -F':' '{print $2}' | tr -d '[:space:]' | sed 's/["\,]/\n/g' | xargs du -sh
```
## Verificar todos containers
```
docker inspect $(docker ps -aq) | grep -i logpath | awk -F':' '{print $2}' | tr -d '[:space:]' | sed 's/["\,]/\n/g'
```


## Listar images nao usadas
```
docker images --filter "dangling=true" -q
```

## Removendo images nao usadas
```
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```


## Remover images de container com exit
`
docker rm $(docker ps -qa --no-trunc --filter "status=exited")
`
