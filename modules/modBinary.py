bin0 = '0'
bin1 = '1'

def changeBin(encryptS):
    bin0 = input("\nWhat is the '0' in the given binary string: ")
    upZero = encryptS.replace(bin0, "0")

    bin1 = input("\nWhat is the '1' in the given binary string: ")
    upOne = upZero.replace(bin1, "1")

    print(f"Updated binary string: {upOne}")
    return upOne

def conv(encryptS, d):
    regBin = None
    while regBin is None and d is False:
        regBin = input("\nTypical binary is made of 0/1's. \nDoes the submitted string follow that [y/n]? ").strip().lower()
        if regBin == 'y':
            regBin = True
        elif regBin == 'n':
            regBin = False
            encryptS = changeBin(encryptS)
        else:
            regBin = None
            print("Invalid option, try again. \n")

    try:
        upSpace = encryptS.replace(" ", "")
        byteChunks = [upSpace[i:i+8] for i in range(0, len(upSpace), 8)]
        result = ''.join([chr(int(byte, 2)) for byte in byteChunks])
        
        # print(f"\nFrom Binary: {result}\n")
        return result
    
    except Exception:
        # print(f"\nInvalid binary string: {encryptS}")
        return False 