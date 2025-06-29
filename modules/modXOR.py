def shiftLogic(encryptS, key):
    try: 
        result = ''.join(chr(b ^ int(key)) for b in (encryptS.encode('latin1')))
        print(f"XOR {key}: {result}")
        return result
    except Exception as e:
        print(f"Error decoding with key {key}: {e}")
        return encryptS

def conv(encryptS):
    result = ""
    key = 0
    bruteForce = False
    choice = None
    
    while key == 0:
        inp = input("\nDo you know the key? \nEnter key (0-255) or [n]? ").strip().lower()
        if inp == 'n':
            bruteForce = True
            break
        elif inp.isdigit():
            if 0 <= int(inp) <= 255:
                key = inp
            else:
                print("Key must be between 0 and 255.\n")
        else:
            print("Invalid input, try again. \n")
    
    print(f"\nEncrypted string: {encryptS}\n")
    keys = range(1, 255) if bruteForce else [key]
    for key in keys:
        if bruteForce and (key % 10 == 0):
            while choice == None:
                choice = input("\n  [#]XOR key to continue with\n  [c]Continue brute force \n  [e]Exit \nChoice: ")
                if choice == 'c':
                    choice = None
                    print(" ")
                    break
                elif choice == 'e':
                    return encryptS
                elif choice.isdigit():
                    if 0 <= int(choice) <= 255:
                        key = choice
                        result = shiftLogic(encryptS, key)
                        return result
                    else:
                        print("Key must be between 0 and 255.\n")
                else: 
                    print("Invalid input, try again. \n")
        result = shiftLogic(encryptS, key)
        
    print(" ")
    return result