import string
import random

chars = " "  + string.digits + string.ascii_letters
chars = list(chars)
key = ['d', 'H', 'v', 'b', 'r', '7', 'T', 'S', 'M', 'E', 'W', 'A', 'K', 'e', 'i', 'C', 'G', 'w', ' ', 'P', 'y', 'x', 'R', 'q', 'U', 'B', 'g', 'O', 'k', 'N', '0', 't', 'u', 'X', 'L', '4', '8', 'n', 'Q', 'J', 'h', 'o', 'V', '5', 'I', 'l', 's', '9', 'z', 'f', 'Z', 'F', 'c', '1', 'p', 'j', 'Y', 'D', 'm', '3', '6', '2', 'a']

class crypt :
    #ENCRYPT
    def __init__(self, _text, type = "password") :
        self.__text = _text 
        self.type = type
        #add algorithm for Pins

    def encrypt(self):
        self.__cipher_text = ""

        for letter in self.__text:
            if letter in string.punctuation :
                self.cipher_text += letter
            else :
                index = chars.index(letter)
                self.__cipher_text += key[index]

        return self.__cipher_text

    #DECRYPT
    def decrypt(self):
        plain_text = ""

        if type(self.__text) == list or type(self.__text) == tuple :
           
            for word in self.__text:                
                for letter in word:
                    if letter in string.punctuation :
                        plain_text += letter
                    else :
                        index = key.index(letter)
                        plain_text += chars[index]
                plain_text+=" "
            return plain_text

        else :
        
            for letter in self.__text:
                if letter in string.punctuation :
                    plain_text += letter
                else :
                    index = key.index(letter)
                    plain_text += chars[index]

            return plain_text
        
print(crypt("Password").encrypt())
