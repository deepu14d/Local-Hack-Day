code={ 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-', ' ':' '}
    
def to_morse_code(text):
    morse_code=""
    for x in text:
        morse_code += code[x.upper()]
    return morse_code

def to_text(morse):
    morse += ' '
 
    decipher = ''
    citext = ''
    for letter in morse:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(code.keys())[list(code
                .values()).index(citext)]
                citext = ''
 
    return decipher

text = input("Enter the text for encoding in Morse Code: ")
print(to_morse_code(text))
print("\n\n")
morse = input("Enter morse code for decoding into normal text: ") #give space between words
print(to_text(morse))