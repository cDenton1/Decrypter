#!/usr/bin/env python3
import argparse
import importlib.util
import os
import sys
import datetime
import math
from collections import Counter

# option menus
import menus.menuHelp as menuHelp
import menus.menuMods as menuMods

# ANSI colour mapping
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

modules = []

if str(os.name) == 'posix':
    SCRIPT_DR = os.path.dirname(os.path.realpath(__file__))
    MOD_PATH = os.path.join(SCRIPT_DR, 'modules')
else:
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
    # modules = []
    count = -1      # total count of files in the modules subfolder (-1 for __pychache__)
    iCount = 0      # count of all successfully imported modules

    print(f"\n{BLUE}[*] Loading modules...{RESET}")
    for fName in os.listdir(MOD_PATH):                          # checks /modules/
        count += 1
        if fName.startswith("mod") and fName.endswith(".py"):   # starts with mod and ends with .py
            name = fName[:-3]                                   # removes mod
            fPath = os.path.join(MOD_PATH, fName)               # full path
            
            spec = importlib.util.spec_from_file_location(name, fPath)
            if not spec or not spec.loader:                                 # spec/error handling
                print(f"{GREEN}[-] Skipping {name}: No loader or spec.{RESET}")
                continue

            try:                                                            # more error handling
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, "conv") and callable(mod.conv):             # checks if it has 'conv' function
                    iCount += 1
                    modules.append(mod)                                     # adds to the list of modules
                else:
                    print(f"{GREEN}[-] Skipping {name}: No 'conv()' function.{RESET}")
            except Exception as e:
                print(f"{RED}[!] Failed to load {name}: {e}{RESET}")
    
    print(f"{BLUE}[*] Loaded {iCount}/{count} modules.{RESET}")
    return modules

def dOptList(modules, optList):      # creates option list of tuples for printing
    for i, m in enumerate(modules):
        optList.append((i + 1, m.__name__[3:]))
    return optList

# call decryption module
def callMod(opt, encryptS, file, modules, optList):
    d = False
    try:
        mod = modules[opt - 1]                              # map chosen module
        ret = mod.conv(encryptS, d)                            # store retured result
        if ret is False:
            print(f"\nInvalid {optList[opt - 1][1]} string: {encryptS}")    # print if invalid
            ret = encryptS
        else:
            print(f"\nFrom {optList[opt - 1][1]}: {ret}")     # print the module and returned string
    
    except Exception:
        return False                    # return false if not a valid module
    
    while True:             # RED/RESET: ANSI escape and colour codes predefined
        run = input(f"  {RED}[c]{RESET}Continue with another technique\n  " \
        f"{RED}[r]{RESET}Revert back a step\n  {RED}[e]{RESET}Exit \nChoice: ").strip().lower()
        
        if run == 'e':                                                              # if exit
            print(f"Final string: {ret}\n")                                         # print final
            if file != None:                                                        # check if output file
                file.write(f"\nFinal string: \n{optList[opt - 1][1]}: {ret}\n")     # write to file
            exit(0)

        elif run == 'c':                                            # if continue
            if file != None:                                        # check if output file
                file.write(f"\n{optList[opt - 1][1]}: {ret}\n")     # write to file
            return ret                                              # return result string
        
        elif run == 'r':                                    # if revert
            print(f"Revert back to string: {encryptS}")     # print string before decryption attempt
            return encryptS                                 # return current string
        
        else:
            print("\nInvalid option, try again.")

def readFile(fpath):            # if input file
    file = open(fpath, "r")     # store and read file
    return file.readline()      # read line, store string

def asciiTitle():     # terminal ascii title output
    print(" ___     ____    __    ___            ___   ______  ____  ___    ")
    print("||  \\\\  ||     //  \\\\ ||  \\\\  \\\\  // ||  \\\\   ||   ||    ||  \\\\  ")
    print("||   || ||___ ||      ||__//   \\\\//  ||__//   ||   ||___ ||__//  ")
    print("||   || ||    ||      ||  \\\\    //   ||       ||   ||    ||  \\\\  ")
    print("||__//  ||___  \\\\__// ||   \\\\  //    ||       ||   ||___ ||   \\\\ ")

    #  ___     ____    __    ___            ___   ______  ____  ___  
    # ||  \\  ||     //  \\ ||  \\  \\  // ||  \\   ||   ||    ||  \\
    # ||   || ||___ ||      ||__//   \\//  ||__//   ||   ||___ ||__//        output of
    # ||   || ||    ||      ||  \\    //   ||       ||   ||    ||  \\        the above
    # ||__//  ||___  \\__// ||   \\  //    ||       ||   ||___ ||   \\
    
    return

def entropy(encryptS, optList):      # entropy detection
    frequency = Counter(encryptS)
    total_characters = len(encryptS)
    entropy = -sum((count / total_characters) * math.log2(count / total_characters) 
                   for count in frequency.values())
    print(f"\nEntropy: {entropy}")

    d = True
    for idx, opt in optList:                              # map chosen module
        mod = modules[idx - 1]
        ret = mod.conv(encryptS, d)                            # store retured result
        if ret is not False and ret is not True:
            if ret != "":
                print(f"  From {optList[idx - 1][1]}: {ret}")     # print the module and returned string
        # elif ret is False:
        #     print(f"  INVALID {optList[idx - 1][1]} string")    # print if invalid

def main(argv):
    asciiTitle()
    
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
    optList = []

    modules = loadMods()
    optList = dOptList(modules, optList)

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
        file = open(fpath, "w")                             # open as append
        file.write(f"Encrypted String: {encryptS}\n")       # write given encryption string

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
        
        print(f"\nDecode Options: \n{RED}[e]{RESET} Exit")      # print list header and exit option
        if optPage > 1:                                         # check if not the first page
            print(f"{RED}[p]{RESET} Previous Page")             # print previous page option

        # for n, opt in pageOpt:                                  # loop through options
        #     print(f"  {BLUE}[{n}]{RESET} {opt}")                # print

        # leftC = pageOpt[:4]
        # rightC = pageOpt[4:]

        # while len(rightC) < len(leftC):
        #     rightC.append(('', ''))

        # for i in range(len(leftC)):
        #     left = leftC[i]
        #     right = rightC[i]
        #     leftS = f"{BLUE}[{left[0]}]{RESET} {left[1]}" if left[0] else ""
        #     rightS = f"{BLUE}[{right[0]}]{RESET} {right[1]}" if right[0] else ""
        #     print(f"  {leftS}\t\t{rightS}")

        for n, name in pageOpt:
            print(f"  {BLUE}[{n}]{RESET} {name}")

        print(f"{RED}[d]{RESET} Detect")                        # print the detect option
        if optEnd < len(optList):                               # check if not the last page
            print(f"{RED}[n]{RESET} Next Page")                 # print next page option
        opt = input("Choice: ").strip().lower()                 # store user choice

        if opt == 'n' and optEnd < len(optList):    # if next page chosen
            optPage += 1                            # move to next page
        elif opt == 'p' and optPage > 1:            # if previous page chosen
            optPage -= 1                            # move back a page
        elif opt == 'e':                            # if exit chosen
            print(f"Final string: {encryptS}\n")    # print current/final string
            exit(0)
        elif opt == 'd':                            # if detect is chosen
            entropy(encryptS, optList)                       # call entropy function
        elif opt.isdigit():                                                 # if number is chosen
            run = callMod(int(opt), encryptS, file, modules, optList)       # call run with option, encrypted string, and file path
            if run == False:                                                # if false
                print("\nInvalid option, try again.")                         # invalid option
            else:
                encryptS = run                          # store returned string
                optPage = 1                             # reset to first page
        else: 
            print("\nInvalid input, try again.")

if __name__ == '__main__':\
    main(sys.argv)