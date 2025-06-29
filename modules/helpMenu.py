def main():
    print("Welcome to Decrypter! \nUsage: decrypter <encrypted string>\n")

    print("Strings with SPACES require SINGLE QUOTES\n")

    print("Current Available Modules:\n  "
    "[1]Base64 \t- Decode Base64 strings\n  "
    "[2]ROT13 \t- Decode ROT13 encoded strings; includes options for digit shifting and brute forcing\n  "
    "[3]Binary \t- Decode Binary strings; including options for strings not made of 0/1's\n  "
    "[4]Hex \t- Decode Hex encoded strings\n  "
    "[5]Hexdump \t- Decode strings from Hexdumps\n  "
    "[6]URL Decode \t- Decode URI/URL percent encodings to raw values\n " 
    "[7]Morse Code \t- Decode strings of morse code\n" 
    "[8]XOR \t- Decipher a string with a known key or brute force")
    
    return