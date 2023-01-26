def cipher(string, shift):
    lst = list(string)
    ordinal = []
    
    for item in lst:
        ordinal.append(ord(item))

    shifted = []    
    
    for num in ordinal:
        shifted.append(num + shift)
    
    num_wrap = []

    for i in shifted:
        if i >= 65 and i <= 90:
            num_wrap.append(((i - 65 + shift) % 26) + 65)
        elif i >= 97 and i <= 122:
            num_wrap.append(((i - 97 + shift) % 26) + 97)
        else:
            num_wrap.append(i)

    letters_shifted = []
    
    for num in num_wrap:
        letters_shifted.append(chr(num))

    code = ''.join(letters_shifted)
    print(code)

cipher("test test", 1)

            






  
  #32 is a space
