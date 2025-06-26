#!/usr/bin/env python3
import argparse
import importlib    #.util
import os
import sys

# decryption modules below
import modules.modBase64 as modBase64
import modules.modROT13 as modROT13

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
            exit(2)
        elif run == 'c':
            print(f"String: {ret}")
            return ret
        elif run == 'r':
            print(f"String: {encryptS}")
            return encryptS
        else:
            print("Invalid option, try again.")

def helpMenu():
    print("Welcome to Decrypter! \nDecrypter is a command line tool for decrypting a string or message in as many steps as you want. " \
    "The tool is made up of a main file, and then separate modules for each decryption method. It is in the early development " \
    "stages and very much still a work in progress; but I hope you see it's potential.\n")

    print("Usage: decrypter <encrypted string>\n")

    print("Current Available Modules: \n  [1]Base64 - ... \n  [2]ROT13- ...")
    return

def main(argv):
    if len(argv) < 2:
        print("Usage: decrypter <encrypted string> \nFor Help: decrypter -h")
        sys.exit(1)
    if argv[1] == '-h':
        helpMenu()
        sys.exit(3)

    encryptS = argv[1]

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
            exit(2)
        elif opt.isdigit():
            run = callMod(int(opt), encryptS)
            if run == False:
                print("Invalid option, try again.")
            else:
                encryptS = run
        else:
            print("Invalid input, try again.")

if __name__ == '__main__':
    main(sys.argv)