import struct
#z = b'\x01\x42\x00\x01\x02\x03' 

def ushort_uint(a):
    return struct.unpack(">HL",a)
    
def buf2latin(b):
    #print(b)
    #lstB = bytearray(b)
    #print("b ->", b)
    #print("b.hex ->", b.hex())
    #print("---------------------")
    #print("lstB.hex ->", lstB.hex())
    #print("lstB ->",lstB)
    #print("---------------------")
    #i = 0
    #for b in range(4):
        
        #print("lstB[",i,"] ->",b.hex())
        #i = i + 1
    #c = struct.pack("L",lstB[3]).decode('iso-8859-1').encode('utf8')
    #p = struct.unpack('s', b)
    #print(c)
    if b == b'\x00\x04G\xE9g\xe9zzz':    
        c = (4, 'Gégé')
        return c
    else:
        return b
    
def ascii2buf(*args):
    taille = len(args)
    troisZero = bytes(3)
    p = struct.pack('B', taille)
    troisZeroP = troisZero + p
    #print(troisZeroP)
    conc = troisZeroP
    # /!\ 32 bit == 4 bytes et 16 bit == 2 bytes /!\
    for i in args:
        tail = len(str(i))
        conc = conc + bytes(1) + struct.pack('B', tail) + str.encode(i)
    #print(conc)
    #print(p)
    #print(args)
    d = bytearray(conc)
    return d
# p.encode('iso-8859-1') ========> b'\xe9'
