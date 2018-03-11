##########################

MAXBITS = 8

def invertBits(num):
    return ~ num 

def setBits(num):
    b = 0 
    for i in range(num):
        b = b <<  1 
        b = (b | 1)
    return b

def getBitMask(list):
    mask = 0
    bits = len(list)
    
    while (list):
        mask = mask << 1
        bit = 0 
        if list.pop(0):
            bit = 1   
        mask = (mask | bit)

    return (bits, mask)

def getNBits(bitPos, bitLen, raw_data):
    firstBit = bitPos # 4 
    lastBit = bitPos + bitLen # 10
    
    firstByte = bitPos / MAXBITS
    firstBitInByte = bitPos % MAXBITS
    
    canReadFromCurrByte = MAXBITS - firstBitInByte
    
    if canReadFromCurrByte >= bitLen:
        # read requested bits
        res = (ord(raw_data[firstByte]) >> (MAXBITS - bitLen - firstBitInByte)) & setBits(bitLen)
        # switch off prefix bits 
        # move right extra postfix bits
        return res
    else: 
        res = (ord(raw_data[firstByte]) >> (MAXBITS - canReadFromCurrByte - firstBitInByte)) & setBits(canReadFromCurrByte)
        res = (res << (bitLen - canReadFromCurrByte)) | getNBits(bitPos + canReadFromCurrByte, bitLen - canReadFromCurrByte, raw_data)
        return res     
        

def huffDecode(codeLen, codeData, codes):
    res = None 
    for dec, dTup in codes.items():
        dLen, dData = dTup
        if (codeLen == dLen) and (codeData == dData):
            return dec
    return res
         
         
def decode_read():
    res = list()
    f = open("dataout.1", "rb")
    try:
        byte = f.read(1)
        while byte != "":
            res.append(byte)    
            byte = f.read(1)
    finally:
        f.close()       
    return res         
         

if __name__ == '__main__':
    pass
