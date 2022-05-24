# Martin Vickgren

def formatNameFiled(query_url):
    outString = ""  # empty string to fill
    for i in query_url.split('.'):  # splits at every "." and loops over each part
        outString += chr(len(i)) + i  # length of the string + part of the string
    zero = chr(0)
    one = chr(1)
    outString += zero + zero + one + zero + one  # adds 00101 to the end
    return outString.encode(encoding='utf_8')  # returns as bytes


def attach12(_str):
    zero = chr(0).encode(encoding='utf_8')  # char to byte
    one = chr(1).encode(encoding='utf_8')  # char to byte
    tmp = zero + one + one + zero + zero + one + zero + zero + zero + zero + zero + zero  # 011001000000
    return tmp + _str  # 011001000000 + _str but in bytes
