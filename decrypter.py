#!/usr/bin/env python3
import argparse
import importlib    #.util
import os
import sys

import modules.helpMenu as helpMenu

# decryption modules below
import modules.modBase64 as modBase64
import modules.modROT13 as modROT13
import modules.modBinary as modBinary
import modules.modHex as modHex
import modules.modHexdump as modHexdump
import modules.modURLde as modURLde
import modules.modMorseC as modMorseC
import modules.modXOR as modXOR
import modules.modAtBash as modAtBash
import modules.modOctal as modOctal

decryptMods = [
    (1, modBase64),
    (2, modROT13),
    (3, modBinary),
    (4, modHex), 
    (5, modHexdump),
    (6, modURLde),
    (7, modMorseC),
    (8, modXOR),
    (9, modAtBash),
    (10, modOctal)
]

# region LOAD MODULE FUNCTION FOR LINUX
# COMMENT OUT THE IMPORT LINES ABOVE AND UNCOMMENT .util AND THE FUNCTION BELOW

# def load_module(name):
#     base_path = os.path.dirname(os.path.realpath(__file__))
#     module_path = os.path.join(base_path, 'modules', f'{name}.py')

#     if not os.path.exists(module_path):
#         return None

#     spec = importlib.util.spec_from_file_location(name, module_path)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     return module
# endregion

# region BEGINNING OF CALLMOD FUNCTION FOR LINUX
# REPLACE THE callMod BEFORE THE WHILE LOOP WITH THE BELOW
# def callMod(opt, encryptS):
#     module_map = {
#         1: 'modBase64',
#         2: 'modROT13'
#         3: 'modBinary'
#         # Add more mappings as needed
#     }

#     if opt not in module_map:
#         return False

#     mod = load_module(module_map[opt])
#     if not mod:
#         print(f"[-] Module '{module_map[opt]}' not found.")
#         return False

#     try:
#         ret = mod.conv(encryptS)
#     except Exception as e:
#         print(f"[-] Error running module: {e}")
#         return False
# endregion

def callMod(opt, encryptS):
    try:
        mod = decryptMods[opt - 1][1]
        ret = mod.conv(encryptS)
    except Exception:
        return False
    
    while True:
        # print(f"String: {ret}")       # for debugging
        run = input("  [c]Continue with another technique\n  [r]Revert back a step\n  [e]Exit \nChoice: ").strip().lower()
        if run == 'e':
            print(f"Final string: {ret}\n")
            exit(0)
        elif run == 'c':
            return ret
        elif run == 'r':
            print(f"Revert back to string: {encryptS}")
            return encryptS
        else:
            print("Invalid option, try again.")

def main(argv):
    if len(argv) < 2:
        print("Usage: decrypter <encrypted string> \nFor Help: decrypter -h")
        exit(0)
    if argv[1] == '-h':
        helpMenu.main()
        exit(0)

    encryptS = argv[1]

    optList = ["[1]Base64", "[2]ROT13", "[3]Binary", "[4]Hex", "[5]Hexdump", 
               "[6]URL Decode", "[7]Morse Code", "[8]XOR", "[9]AtBash", "[10]Octal"]
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
            print(f"Final string: {encryptS}\n")
            exit(0)
        elif opt.isdigit():
            run = callMod(int(opt), encryptS)
            if run == False:
                print("Invalid option, try again.")
            else:
                encryptS = run
                optPage = 1
        else:
            print("Invalid input, try again.")

if __name__ == '__main__':
    main(sys.argv)