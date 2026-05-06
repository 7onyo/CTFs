import base64
import subprocess

command = 'unzip Layer-master-v3204.zip'
result = subprocess.run(command, shell=True, capture_output=True, text=True)

i = 2
while True:
    number = str(i).zfill(4)
    command = 'unzip layer_' + number + '.zip'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    i += 1
    if result.returncode != 0:
        break   

with open('flag.txt', 'r') as f:
    flag = f.read()
    flag = base64.b64decode(flag).decode('utf-8')
    print(flag)