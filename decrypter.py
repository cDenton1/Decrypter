#!/usr/bin/env python3
import argparse
import importlib.util
import os
import sys
import datetime

# option menus
import menus.menuHelp as menuHelp
import menus.menuMods as menuMods

MOD_PATH = os.path.join(os.path.dirname(__file__), 'modules')

# region IMPORTS
# original static decryption module imports
# import modules.modBase64 as modBase64
# import modules.modROT13 as modROT13
# import modules.modBinary as modBinary
# import modules.modHex as modHex
# import modules.modHexdump as modHexdump
# import modules.modURLde as modURLde
# import modules.modMorseC as modMorseC
# import modules.modXOR as modXOR
# import modules.modAtBash as modAtBash
# import modules.modOctal as modOctal
# endregion

# dynamic loading for modules
def loadMods():
    modules = []
    for fName in os.listdir(MOD_PATH):                          # checks /modules/
        if fName.startswith("mod") and fName.endswith(".py"):   # starts with mod and ends with .py
            name = fName[:-3]                                   # removes mod
            fPath = os.path.join(MOD_PATH, fName)               # full path
            
            spec = importlib.util.spec_from_file_location(name, fPath)
            if not spec or not spec.loader:                                 # spec/error handling
                print(f"[-] Skipping {name}: No loader or spec.")
                continue

            try:                                                            # more error handling
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, "conv") and callable(mod.conv):             # checks if it has 'conv' function
                    modules.append(mod)                                     # adds to the list of modules
                else:
                    print(f"[-] Skipping {name}: No 'conv()' function.")
            except Exception as e:
                print(f"[-] Failed to load {name}: {e}")
    return modules

def dOptList(modules):      # creates option list for printing
    return [f"[{i + 1}]{m.__name__[3:]}" for i, m in enumerate(modules)]

# call decryption module
def callMod(opt, encryptS, file, modules, optList):
    try:
        mod = modules[opt - 1]          # map chosen module
        ret = mod.conv(encryptS)        # store retured result
    except Exception:
        return False                    # return false if not a valid module
    
    while True:
        run = input("  [c]Continue with another technique\n  [r]Revert back a step\n  [e]Exit \nChoice: ").strip().lower()
        
        if run == 'e':                                                              # if exit
            print(f"Final string: {ret}\n")                                         # print final
            if file != None:                                                        # check if output file
                file.write(f"\nFinal string: \n{optList[opt - 1][3:]}: {ret}\n")    # write to file
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
    parser = argparse.ArgumentParser(description="Modular CLI decryption tool", add_help=False)     # set default help to false
    parser.add_argument("input", nargs="?", help="Encrypted string (or use -f for file input)")     # input
    parser.add_argument("-f", "--file", help="Path to input file")                                  # input file
    parser.add_argument("-o", "--output", action="store_true", help="Write output to dated file")   # output file
    parser.add_argument("-m", "--mods", action="store_true", help="Show modules list")              # mod list
    parser.add_argument("-h", "--help", action="store_true", help="Show help menu")                 # help menu

    args = parser.parse_args()

    if args.help:           # if help option
        menuHelp.main()     # call help menu
        exit(0)
    if args.mods:           # if module option
        menuMods.main()     # call module menu
        exit(0)

    file = None
    modules = loadMods()
    optList = dOptList(modules)

    if args.file:                       # if input file
        encryptS = readFile(args.file)  # store returned string from file
    elif args.input:
        encryptS = args.input
    else: 
        print("Usage: decrypter <encrypted string> [-f <file>] [-o] [-m] [-h]")   # print help message
        exit(0)

    if args.output:
        cDate = datetime.datetime.now().date()              # store date
        fpath = f"decrypter-{cDate}.txt"                    # create filename
        with open(fpath, "w") as file:                      # open file
            file.write(f"Encrypted String: {encryptS}\n")   # write given encryption string
        file = open(fpath, "a")                             # open as append

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
            run = callMod(int(opt), encryptS, file, modules, optList)     # call run with option, encrypted string, and file path
            if run == False:                            # if false
                print("Invalid option, try again.")     # invalid option
            else:
                encryptS = run                          # store returned string
                optPage = 1                             # reset to first page
        else: 
            print("Invalid input, try again.")

if __name__ == '__main__':\
    main(sys.argv)