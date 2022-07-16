# Rsync
rsync -avzhe 'ssh -p 19930' /usr/app/newdir3 tm@179.180.71.239:/mnt/storage1/

# Rsync local
rsync -avzh /usr/app/newdir3 /mnt/storage1/

# Contar arquivos na pasta recursivamente
find /usr/app/newdir3/ -type f | wc -l

# Contar por pasta
find /usr/app/newdir3/ -maxdepth 1 -type d | while read -r dir
do printf "%s:\t" "$dir"; find "$dir" -type f | wc -l; done