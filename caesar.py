def encrypt(text, rot):
    crypt_text = ''
    for i in range(len(text)):
        crypt_text = crypt_text + rotate_character(text[i],rot)
    return(crypt_text)

def rotate_character(char, rot):
    mod_num = rot%26
    if mod_num == 0:
        mod_num = rot
    l_list = []
    if char.isalpha() == True:
        if char.isupper() == True:
            mod_num = (rot + (ord(char) - 65)) % 26
            for i in range(65,91):
                l_list.append(chr(i))
        else:
            mod_num = (rot + (ord(char) - 97)) % 26
            for i in range(97,123):
                l_list.append(chr(i))
        return(l_list[mod_num])
    else:
        return(char)

def alphabet_position(letter):
    l_list = []
    if letter.isupper() == True:
        for i in range(65,91):
            l_list.append(chr(i))
    else:
        for i in range(97,123):
            l_list.append(chr(i))
    return(l_list.index(letter))
