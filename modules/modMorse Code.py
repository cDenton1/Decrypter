morse = {
    # letters
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
    'y': '-.--', 'z': '--..',
    # numbers
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----',
    # special characters
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', 
    '!': '-.-.--', '/': '-..-.', ':': '---...', ';': '-.-.-.', 
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
    '"': '.-..-.', '@': '.--.-.'
}

def conv(encryptS, d):
    try: 
        morseRev = {v: k for k, v in morse.items()}
        words = encryptS.strip().split(' / ')
        dWords = []

        for word in words:
            letters = word.split()
            dLetters = [morseRev.get(letter, '?') for letter in letters]
            dWords.append(''.join(dLetters))
        
        result = ' '.join(dWords)
        # print(f"\nFrom Morse Code: {result}\n")
        return result
    
    except: 
        return False