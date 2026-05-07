# tshark -r challenge3.pcap -T fields -e dns.qry.name | awk 'NR==7 || NR==9 || NR==13 || NR==15 || NR==19 || NR==21' > dns.txt

import base64
import subprocess

command = "tshark -r challenge.pcap -T fields -e dns.qry.name | awk 'NR==7 || NR==9 || NR==13 || NR==15 || NR==19 || NR==21'"
text = subprocess.run(command, shell=True, capture_output=True, text=True)
text = text.stdout

print(text)

text = text.split('.exfil.attacker.test\n')
print(text)

text = [s.split(".")[1] for s in text if len(s.split(".")) > 1]
print(text)

for i in text:
    i += '='
    print(base64.b64decode(i).decode('utf-8'), end='')
