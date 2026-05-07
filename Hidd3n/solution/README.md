
# Solution: Hidd3n

First, I opened `challenge.pcap` with Wireshark. I observed that all the traffic was DNS communication, and certain lines (7, 9, 13, 15, 19, and 21) contained subdomains that looked like base64 encoded text.

To automate the extraction, I wrote a Python script. Inside the script, I used the following `tshark` command as a subprocess to extract the DNS query names from those specific lines:
```bash
tshark -r challenge.pcap -T fields -e dns.qry.name | awk 'NR==7 || NR==9 || NR==13 || NR==15 || NR==19 || NR==21'
```

This command extracted the following output:
```text
01.VVZUSUNT.exfil.attacker.test
02.e2Ruc19u.exfil.attacker.test
03.NG1lZWVl.exfil.attacker.test
04.M3NfY2Fu.exfil.attacker.test
05.X2wzNGtf.exfil.attacker.test
06.ZEF0YX0.exfil.attacker.test
```

Next, I cleaned the data by splitting the strings by `.exfil.attacker.test`. I then removed the sequence numbers and the dots from the beginning of each remaining string. This resulted in a clean array of base64 chunks:
```python
['VVZUSUNT', 'e2Ruc19u', 'NG1lZWVl', 'M3NfY2Fu', 'X2wzNGtf', 'ZEF0YX0']
```

Finally, I concatenated all the strings in the array and decoded the combined string from base64 to reveal the plain text flag.

**Flag:** `UVTICS{dns_n4meeee3s_can_l34k_dAta}`
