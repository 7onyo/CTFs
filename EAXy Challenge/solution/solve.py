def hexToDec(number): 
    return int(number, 16)

def binToDec(number): 
    return int(number, 2)

def decToBin(number): 
    return bin(number)[2:]

def bswap(reg): 

    reg = decToBin(reg)

    regLs = []
    
    regLs.append(reg[0:8])
    regLs.append(reg[8:16])
    regLs.append(reg[16:24])
    regLs.append(reg[24:32])
    
    regLs[0], regLs[3] = regLs[3], regLs[0]
    regLs[1], regLs[2] = regLs[2], regLs[1]


    regLs = ''.join(regLs)
    regLs = binToDec(regLs)
    return regLs

def shr(reg, noBits):
    return reg >> noBits

def shl(reg, noBits):
    return (reg << noBits) & 0xffffffff  

def main():
    eax, edx = 0, 0 #1-4
    eax = hexToDec('0xdeadbeef') #5
    eax = bswap(eax) #6    
    edx = eax #7
    eax = eax & hexToDec('0xf0f0f0f') #8
    edx = edx & hexToDec('0xf0f0f0f0') #9
    edx = shr(edx, 4) #10
    eax = shl(eax, 4) #11
    eax = eax | edx #12
    edx = eax #13
    eax = eax & hexToDec('0x33333333') #14
    edx = edx & hexToDec('0xcccccccc') # 15
    edx = shr(edx, 2) #16
    eax = shl(eax, 2) #17
    eax = eax | edx #18
    edx = eax #19
    eax = eax & hexToDec('0x55555555') #20
    edx = edx & hexToDec('0xaaaaaaaa') #21
    eax = eax + eax #22
    edx = shr(edx, 1) #23
    eax = eax | edx #24

    print('UVTCA{{{}}}'.format(hex(eax)))


 
if __name__ == '__main__':
    main()







