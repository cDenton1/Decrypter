def conv(encryptS, d):
    values = encryptS.strip().split()
    res = []

    try:
        for i in values:
            n = ''.join(chr(int(i, 8)))
            res.append(''.join(n))
        result = ''.join(res)
        # print(f"\nFrom octal: {result}\n")
        return result
    
    except ValueError:
        # print(f"\nInvalid octal string: {encryptS}")
        return False 