# The user can enter either morse code or english words that can be translated
# into the other when the program is run

# The morse code has to be comprised of '.' as the dots and '-' as the dashes
# and have a space between the letters. The space between words are indicated by
# a '/'.
alpha = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I':'..', 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..','1': '.----', '2': '..---', '3': '...--',
 '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
 '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?':'..--..',
 '/': '-..-.', '@':'.--.-.', ' ':'/'}
morse=str()
while True:
    inp=input('enter words or morsecode here\n')
    if inp == 'quit': break
    try:
        if ord(inp[0]) in (45,46,47):
            s=inp.split(' ')
            for morseletter in s:
                for letter,morsevalue in alpha.items():
                    if morseletter==morsevalue:
                        morse+=letter
                    else:continue
        else:
            uinp=inp.upper()
            for code in uinp:
                morse+=' '+alpha[code]
    except ValueError:
        print('please enter a number or character from the alphabet')
        continue
    break
if len(morse)!=0:
    print('morsecode:',morse,)
else:print('There is no morse code')
