from urllib.parse import unquote

def conv(encryptS, d):
    try: 
        decoded = unquote(encryptS)
        # print(f"\nURL Decoded: {decoded}\n")
        return decoded
    except Exception as e:
        # print(f"\nInvalid URL: {encryptS}\n")
        return False