## sudo apt isntall dialog
```
#!/bin/bash
# Requer dialog
while : ; do
    resposta=$(
      dialog --stdout               \
             --title 'Acesso SSH'  \
             --menu 'Selecione o Servidor:' \
            0 0 0                   \
            1 'IDENTIFICA - LALALA' \
            2 'IDENTIFICA - LALALA' \
            3 'IDENTIFICA - LALALA' \
            4 'IDENTIFICA - LALALA' \
            5 'IDENTIFICA - LALALA' \
            6 'IDENTIFICA - LALALA' \
            7 'IDENTIFICA - LALALA' \
            8 'IDENTIFICA - LALALA' \
            9 'IDENTIFICA - LALALA' \
            0 'Sair' )
 
    [ $? -ne 0 ] && break
 
    case "$resposta" in
         1) ssh -p 12345 usuario@10.10.10.10 ;;
         2) ssh -p 12345 usuario@10.10.10.10 ;;
         3) ssh -p 12345 usuario@10.10.10.10 ;;
         4) ssh -p 12345 usuario@10.10.10.10 ;;
         5) ssh -p 12345 usuario@10.10.10.10 ;;
         6) ssh -p 12345 usuario@10.10.10.10 ;;
         7) ssh -p 12345 usuario@10.10.10.10 ;;
         8) ssh -p 12345 usuario@10.10.10.10 ;;
         9) ssh -p 12345 usuario@10.10.10.10 ;;
         0) break ;;
    esac
done
```
