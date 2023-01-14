def encoding(a, dict):
    env = ""
    for x in a:
        y = str(bin(ord(x)))[2:]
        while len(y) < 8:
            y = "0" + y
        env += y
    i = 0
    envdec = ""
    while len(env) > i:
        envdec += str(dict.get(env[i:i+6]))
        i += 6
    return envdec, env
def decoding(b):
    dev = ""
    i = 0
    while len(b) > i:
        dev += chr(int(b[i:i+8], 2))
        i += 8
    return dev
def createdict():
    base64 = {}
    i = 0
    while i < 64:
        x = str(bin(i))[2:]
        while len(x) < 6 :
            x = "0" + x
        if(i <= 25):
            base64[x] = chr(i+65)
        elif (i <= 51):
            base64[x] = chr(i+71)
        elif (i <= 61):
            base64[x] = chr(i-4)
        i += 1
    base64[62] = "+"
    base64[63] = "/"
    return base64
base64dict = createdict()
value = "Witam w nowym swiecie"
print("Value before encoding: " + value)
encodedValue, binaryOfEncodedValue = encoding(value, base64dict)
print("Encoded value: " + encodedValue)
#Brak czasu na zmiane wartości encodedValue na binary w funkcji
decodedValue = decoding(binaryOfEncodedValue)
print("Decoded value: " + decodedValue)
