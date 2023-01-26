def cipher(string, shift):
    code = ""

    for i in range(0, len(string)):
        letter = string[i]
    
        if letter == " ":
            code+=" "
        elif (letter.isupper()):
            code += chr((ord(letter) + shift-65) % 26 + 65)
        else:
            code += chr((ord(letter) + shift-97) % 26 + 97)

    print(code)

cipher("Lorem ipsum dolor sit amet", 1)
cipher("Lorem ipsum dolor sit amet", 10)
cipher("Lorem ipsum dolor sit amet", 15)

def decode(string, shift):
    decoded = ""

    for i in range(0, len(string)):
        letter = string[i]
    
        if letter == " ":
            decoded+=" "
        elif (letter.isupper()):
            decoded += chr((ord(letter) - shift-65) % 26 + 65)
        else:
            decoded += chr((ord(letter) - shift-97) % 26 + 97)
    
    print(decoded)

decode("Mpsfn jqtvn epmps tju bnfu", 1)
decode("Vybow szcew nyvyb csd kwod", 10)
decode("Adgtb xehjb sdadg hxi pbti", 15)
