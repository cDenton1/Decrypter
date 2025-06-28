import re

def conv(encryptS):
    hexBytes = []
    cleanLine = encryptS.split('|')[0].strip()

    parts = cleanLine.split()
    hexPart = parts[1:]

    for val in hexPart:
        if re.fullmatch(r'[0-9a-fA-F]{2}', val):
            hexBytes.append(val)

    try:
        byteString = bytes.fromhex("".join(hexBytes))
        decoded = byteString.decode('utf-8')
        print(f"\nFrom Hexdump: {decoded}\n")
        return decoded
     
    except Exception as e:
        print(f"\nInvalid hexdump: {encryptS}")
        return encryptS 