s = 'VWUJDT{X3md0n3}'
s = list(s)
for i in range(len(s)):
    if ((s[i] == '{') or (s[i] == '}')):
        continue
    if (s[i] in '0123456789'):
        continue    
    s[i] = chr(ord(s[i]) - 1)
print(''.join(s))