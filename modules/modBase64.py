import base64
import binascii

def conv(encryptS, d):
    try:
        decoded = base64.b64decode(encryptS).decode('utf-8')
        # print(f"\nFrom Base64: {decoded}\n")
        return decoded
    
    except (binascii.Error, UnicodeDecodeError):
        # print(f"\nInvalid base64 string: {encryptS}")
        return False 