def shiftLogic(encryptS, shift, digShift):
    result = ""
    for char in encryptS:
        if 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif digShift == True and char.isdigit():
            shifted = str((int(char) + shift) % 10)
        else:
            shifted = char
        result += shifted
    print(f"ROT key {shift}")
    return result

def conv(encryptS, d):
    if d is True:
        return True
    else:
        result = ""
        digShift = None
        while digShift == None:
            digShift = input("\nDefault only shifts letters. \nShift digits [y/n]? ").strip().lower()
            if digShift == 'y':
                digShift = True
            elif digShift == 'n':
                digShift = False
            else:
                digShift = None
                print("Invalid option, try again. \n")

        bruteForce = None
        while bruteForce == None:
            bruteForce = input("\nDefault only shifts 13, brute force tries every possible shift. \nBrute force [y/n]? ").strip().lower()
            if bruteForce == 'y':
                bruteForce = True
            elif bruteForce == 'n':
                bruteForce = False
            else:
                bruteForce = None
                print("Invalid option, try again. \n")

        print(f"\nEncrypted string: {encryptS}\n")
        shifts = range(1, 26) if bruteForce else [13]
        for shift in shifts:
            result = shiftLogic(encryptS, shift, digShift)
        
        if bruteForce == True:
            shift = int(input("\nEnter ROT shift # to continue with: "))
            result = shiftLogic(encryptS, shift, digShift)
            print(" ")
        
        return result