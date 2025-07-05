import os

def main():
    print("Welcome to Decrypter! \nUsage: decrypter <encrypted string> [-f <file>] [-o] [-m] [-h]\n")

    print("Options: \n " \
    "-f \t File input, replace encrypted string with filename \n " \
    "-o \t File output, print steps and decrypted strings to an output file\n " \
    "-m \t List available modules and related info\n " \
    "-h \t Output help menu\n")

    print("Strings with SPACES require SINGLE QUOTES\n")

    osN = os.name
    if osN == 'posix':
        print("man decrypter \t- For more info\n")
    
    return