MorseCode = {'A': '.-', 'B': '-...', 'C': '-.-.',
             'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '-.-.',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', ' ': ' ',
             '7': '--...', '8': '---..', '9': '----.', '0': '-----',
             '.':'', '-':'', '/':''
             }


def zmorse(text):
    a = ''
    text = text.upper().split()
    for i in text:
        for j in i:
            a += MorseCode[j] + ' '
        a += '/'
    return a[:-1]


def rmorze(code):
    code = [c.split() for c in code.split('/')]
    t = ''
    for x in code:
        for i in x:
            for j in MorseCode.keys():
                if MorseCode[j] == i:
                    t += j
                    break
        t += ' '
    return t.lower()
##############################################

alpha = 'abcdefghijklmnopqrstuvwxyz'
def zc(s, n):
    n = int(n)
    s = s.strip()
    res = ''
    for c in s:
        if c == ' ' or c in '1234567890':
            res += c
        else:
            res += alpha[(alpha.index(c) + n) % len(alpha)]
    return res

def rc(s, n):
    n = -int(n)
    s = s.strip()
    res = ''
    for c in s:
        if c == ' ' or c in '1234567890':
            res += c
        else:
            res += alpha[(alpha.index(c) + n) % len(alpha)]
    return res
###########################################################
def zb(s):
    n = []
    for i in s:
        n.append(bin(ord(i))[2:])
    return " ".join(n)

def rb(s):
    n = s.split()
    r = ''
    for i in n:
        r += chr(int(str(i), 2))
    return r
