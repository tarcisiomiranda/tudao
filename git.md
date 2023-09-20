```
root@xtk /srv/salt/srv/salt/salt_inventory (tags)$ git pull
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint: 
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint: 
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

```
O erro que você está vendo é causado porque você tem alterações locais em sua branch que ainda não foram sincronizadas com a branch remota. O Git está pedindo para você decidir como deseja reconciliar as diferenças entre as duas branches quando você faz um 
```

### Há três opções principais:

```
Merge (Mesclar): Isso criará um novo commit de mesclagem em sua branch local, combinando as alterações do remoto com suas alterações locais.
Rebase: Em vez de criar um novo commit de mesclagem, o rebase irá "reaplicar" seus commits locais por cima dos commits do remoto. Isso cria um histórico linear, mas pode ser mais complexo de lidar se você não estiver familiarizado com o rebase.
Fast-forward only: Isso só funcionará se suas alterações locais estiverem diretamente à frente das alterações remotas, sem divergências.
Para resolver o problema, você pode escolher uma das opções acima. Aqui estão os passos para cada opção:
```

## Merge:
```
git pull --no-rebase
```

## Rebase:
```
git pull --rebase
```

## Fast-forward only:
```
git pull --ff-only
```

```
Se você deseja definir um comportamento padrão para evitar essa mensagem no futuro, pode usar um dos seguintes comandos:

Para definir merge como padrão:


git config pull.rebase false
Para definir rebase como padrão:


git config pull.rebase true
Para definir fast-forward only como padrão:


git config pull.ff only
Se você optar por usar o 
rebase e encontrar conflitos, precisará resolvê-los manualmente e depois continuar o rebase usando 
git rebase --continue. Se você não estiver familiarizado com o processo de rebase e resolver conflitos, talvez seja mais fácil usar a opção de mesclagem.
```
