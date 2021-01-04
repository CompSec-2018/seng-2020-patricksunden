import codecs
import string

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    s = s.ljust(1000, 'k') #Pad the string

    for c in s:
        if c == '+' or c == '-' or c == 'ä' or c == 'å' or c == 'ö':#if the input is one of these, raise ValueError
            raise ValueError

        if c in digitmapping:
            crypted+=digitmapping[c]
        elif c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        
        

    return crypted[:origlen] #returning only the wanted length

def decode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    decrypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            if c.isupper():
                c=c.lower()
            decrypted += codecs.decode(c, 'rot13')
        elif c in digitmapping:
            decrypted += digitmapping[c]
        else:
            raise ValueError

    return decrypted

