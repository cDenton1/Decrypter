#!/usr/bin/env python3
import argparse
import importlib
import sys

# decryption modules below
import modBase64
import modROT13

def callMod(opt, encryptS):
    if opt == 1:
        ret = modBase64.conv(encryptS)
    elif opt == 2:
        ret = modROT13.conv(encryptS)
    else:
        return False
    
    while True:
        run = input("  [c]Continue \n  [r]Revert \n  [e]Exit \nChoice: ").strip().lower()
        if run == 'e':
            print(f"Final string: {ret}\n")
            exit()
        elif run == 'c':
            print(f"String: {ret}")
            return ret
        elif run == 'r':
            print(f"String: {encryptS}")
            return encryptS
        else:
            print("Invalid option, try again.")

def main(encryptS):    
    optList = ["[1]Base64", "[2]ROT13", "[3]Binary", "[4]Hex", "[5]Placeholder", "[6]Placeholder"]
    optPerPage = 5
    optPage = 1
    opt = None

    while opt != 'e': 
        optStart = (optPage - 1) * optPerPage
        optEnd = optStart + optPerPage
        pageOpt = optList[optStart:optEnd]
        
        print("\nDecode Options: \n[e]Exit")
        if optPage > 1:
            print("[p]Previous Page")
        for opt in pageOpt:
            print("  ", opt)
        if optEnd < len(optList):
            print("[n]Next Page")
        opt = input("Choice: ").strip().lower()

        if opt == 'n' and optEnd < len(optList):
            optPage += 1
        elif opt == 'p' and optPage > 1:
            optPage -= 1
        elif opt == 'e':
            exit()
        elif opt.isdigit():
            run = callMod(int(opt), encryptS)
            if run == False:
                print("Invalid option, try again.")
            else:
                encryptS = run
        else:
            print("Invalid input, try again.")

if __name__ == '__main__':
    encryptS = sys.argv[1]
    main(encryptS)