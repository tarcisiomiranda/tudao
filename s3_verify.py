import os
import time
import datetime

# Timedate
now = datetime.datetime.now()
human_date = now.strftime('%d-%m-%Y_%H:%M:%S')

# Arquivos
dir_path = "/temp/s3_script/"
dir_file = "/temp/s3_script/s3.pid"
if not os.path.exists(os.path.dirname(dir_path)):
    os.makedirs(os.path.dirname(dir_path))

# File exist
if os.path.isfile(dir_file):
    print("Pulando a execucao, processo em andamento")
    exit()

# Create pid file
with open(dir_file, "w") as f:
    f.write('{}'.format(now.strftime('%d-%m-%Y_%H:%M:%S')))


time.sleep(5)

# Remove o arquivo
os.remove(dir_file)
print('Arquivo removido.')
