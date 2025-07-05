#!/usr/bin/env python3
import argparse
import importlib    #.util
import os
import sys
import datetime

# region MENU IMPORTS
# option menus
import menus.menuHelp as menuHelp
import menus.menuMods as menuMods
# endregion

# region MODULE IMPORTS
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
# endregion

# module mapping
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

# option list of modules
optList = ["[1]Base64", "[2]ROT13", "[3]Binary", "[4]Hex", "[5]Hexdump", "[6]URL Decode", "[7]Morse Code", "[8]XOR", "[9]AtBash", "[10]Octal"]

# call decryption module
def callMod(opt, encryptS, file):
    try:
        mod = decryptMods[opt - 1][1]   # map chosen module
        ret = mod.conv(encryptS)        # store retured result
    except Exception:
        return False                    # return false if not a valid module
    
    while True:
        run = input("  [c]Continue with another technique\n  [r]Revert back a step\n  [e]Exit \nChoice: ").strip().lower()
        
        if run == 'e':                                                              # if exit
            print(f"Final string: {ret}\n")                                         # print final
            if file != None:                                                        # check if output file
                file.write(f"\nFinal string: \n{optList[opt - 1][4:]}: {ret}\n")    # write to file
            exit(0)

        elif run == 'c':                                            # if continue
            if file != None:                                        # check if output file
                file.write(f"\n{optList[opt - 1][4:]}: {ret}\n")    # write to file
            return ret                                              # return result string
        
        elif run == 'r':                                    # if revert
            print(f"Revert back to string: {encryptS}")     # print string before decryption attempt
            return encryptS                                 # return current string
        
        else:
            print("Invalid option, try again.")

def readFile(fpath):            # if input file
    file = open(fpath, "r")     # store and read file
    return file.readline()      # read line, store string

def main(argv):
    file = None
    if len(argv) < 2:                                                           # check if arguments
        print("Usage: decrypter <encrypted string> \nFor Help: decrypter -h")   # print help message
        exit(0)

    if argv[1] == '-h':     # if help option
        menuHelp.main()     # call help menu
        exit(0)
    elif argv[1] == '-m':   # if module option
        menuMods.main()     # call module menu
        exit(0)
    elif argv[1] == '-f':           # if input file
        fpath = argv[2]             # store file path
        encryptS = readFile(fpath)  # store returned string from file
    else:
        if argv[1] == '-o':                                     # if output file
            encryptS = argv[2]                                  # store encryption string

            cDate = datetime.datetime.now().date()              # store date
            fpath = f"decrypter-{cDate}.txt"                    # create filename
            with open(fpath, "w") as file:                      # open file
                file.write(f"Encrypted String: {encryptS}\n")   # write given encryption string

            file = open(fpath, "a")                             # open as append
        else:
            encryptS = argv[1]  # store encrypted string
    
    # option page functionality
    optPerPage = 5
    optPage = 1
    opt = None

    # run if option not exit
    while opt != 'e': 
        # option page functionality
        optStart = (optPage - 1) * optPerPage
        optEnd = optStart + optPerPage
        pageOpt = optList[optStart:optEnd]
        
        print("\nDecode Options: \n[e]Exit")        # print list header and exit option
        if optPage > 1:                             # check if not the first page
            print("[p]Previous Page")               # print previous page option
        for opt in pageOpt:                         # loop through options
            print("  ", opt)                        # print
        if optEnd < len(optList):                   # check if not the last page
            print("[n]Next Page")                   # print next page option
        opt = input("Choice: ").strip().lower()     # store user choice

        if opt == 'n' and optEnd < len(optList):    # if next page chosen
            optPage += 1                            # move to next page
        elif opt == 'p' and optPage > 1:            # if previous page chosen
            optPage -= 1                            # move back a page
        elif opt == 'e':                            # if exit chosen
            print(f"Final string: {encryptS}\n")    # print current/final string
            exit(0)
        elif opt.isdigit():                             # if number is chosen
            run = callMod(int(opt), encryptS, file)     # call run with option, encrypted string, and file path
            if run == False:                            # if false
                print("Invalid option, try again.")     # invalid option
            else:
                encryptS = run                          # store returned string
                optPage = 1                             # reset to first page
        else: 
            print("Invalid input, try again.")

if __name__ == '__main__':
    main(sys.argv)