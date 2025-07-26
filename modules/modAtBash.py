def conv(encryptS, d):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    revAlph = alph[::-1]
    transTab = str.maketrans(alph + alph.upper(), revAlph + revAlph.upper())

    result = encryptS.translate(transTab)

    # print(f"\nFrom AtBash: {result}\n")
    return result