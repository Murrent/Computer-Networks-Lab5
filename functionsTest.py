# Martin Vickgren

import msgFunctions

print(msgFunctions.formatNameFiled("bbc.co.uk"))
print(msgFunctions.formatNameFiled("facebook.com"))
print(msgFunctions.formatNameFiled("mixteco.utm.mx"))
print(msgFunctions.formatNameFiled("eluniversal.com.mx"))

print(msgFunctions.attach12(msgFunctions.formatNameFiled("bbc.co.uk")))
print(msgFunctions.attach12(msgFunctions.formatNameFiled("facebook.com")))
print(msgFunctions.attach12(msgFunctions.formatNameFiled("mixteco.utm.mx")))
print(msgFunctions.attach12(msgFunctions.formatNameFiled("eluniversal.com.mx")))
