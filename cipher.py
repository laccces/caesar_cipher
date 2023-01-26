def cipher(string, shift):
    lst = list(string)
    ordinal = []
    
    for item in lst:
        ordinal.append(ord(item))

    shifted = []        
    for num in ordinal:
        if num == 32:
            shifted.append(num)
        else: 
            shifted.append(num + shift)
    
    # num_wrap = []
    # for i in shifted:
    #     if 65 <= i <= 90:
    #         num_wrap.append(((i - 65 + shift) % 26) + 65)
    #     elif 97 <= i <= 122:
    #         num_wrap.append(((i - 97 + shift) % 26) + 97)
    #     else:
    #         num_wrap.append(i)

    letters_shifted = []
    for num in shifted:
        letters_shifted.append(chr(num))

    code = ''.join(letters_shifted)
    print(code)

cipher("Lorem ipsum dolor sit amet", 1)
cipher("Lorem ipsum dolor sit amet", 10)
cipher("Lorem ipsum dolor sit amet", 15)
#def decode(string, shift):
