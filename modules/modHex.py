def conv(encryptS, d):
    try:
        decoded = bytes.fromhex(encryptS).decode('utf-8')
        # print(f"\nFrom Hex: {decoded}\n")
        return decoded
     
    except Exception as e:
        # print(f"\nInvalid hex string: {encryptS}")
        return False 