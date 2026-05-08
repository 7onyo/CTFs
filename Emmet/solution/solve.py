givenString = "TTWGD}j<z=8~R>iO%'&'xt{a8g"
r8b = 1
for i in range(len(givenString)):
    posInAscii = ord(givenString[i]) ^ r8b
    print(chr(posInAscii), end = '')
    r8b += 1