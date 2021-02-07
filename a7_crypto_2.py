#Python program to print the encrypted string
# Author: Jay Varan

import string
import random
from random import choice

#String to be encrypted
quote = "An ounce of practice is worth a thousand words."

#Encrypted string
cryptedStr = ""

#Converting the quote to list,creating ordered list and shuffling
quote_list = list(quote.upper())
order_list = list(string.ascii_uppercase)
random_list = list(string.ascii_uppercase)
random.shuffle(random_list)

#Loop through the quote to encrypt
for chrValue in quote_list:
    indexVal = -1
    if chrValue in order_list:
        indexVal = order_list.index(chrValue)
    if indexVal != -1:        
        cryptedStr = cryptedStr + random_list[indexVal]
    else:
        cryptedStr = cryptedStr + chrValue

#Printing the output
print("Quote: ")
print(quote)
print("Crypto Quote string: ")
print(cryptedStr) 
print(" Hint -->", cryptedStr[0] , "=" , quote_list[0])
