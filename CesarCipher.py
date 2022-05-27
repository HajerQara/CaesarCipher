# Name: Hajer Qara
# Date: 5/29/2022
# File Name: CesarCipher.py

# Cesar Cipher was an past assignment that enabled a user 
# to input a string of text to encrypt or decrypt
# Note: Users are advised to use uppercase 'E' and uppercase 'D' when making a selection 

def encryptstr(message):
    #declare variables
    newstring=str()
    ascii_letter_value=int()
    one_letter=str()
    new_ascii_value=int()
    #loop to assign new ASCII value
    for index in range(0,len(message)):
        one_letter= message[index]
        ascii_letter_value=ord(one_letter)
        #checking if the letter is Z or z
        if ascii_letter_value==122:
            new_ascii_value=97
        elif ascii_letter_value==90:
            new_ascii_value=65
        #assigning a new ascii value if not Z or z
        else:
            new_ascii_value= ascii_letter_value + 1
        #creating the new string
            newstring= newstring + chr(new_ascii_value)
    print(newstring)

    return newstring

def decryptstring(message):
    newstring=str()
    ascii_letter_value=int()
    one_letter=str()
    new_ascii_value=int()
    #loop to assign new ASCII value
    for index in range(0,len(message)):
        one_letter= message[index]
        ascii_letter_value=ord(one_letter)
        #checking if the letter is Z or z
        if ascii_letter_value==97:
            new_ascii_value=122
        elif ascii_letter_value==65:
            new_ascii_value=90
        #assigning a new ascii value if not Z or z
        else:
            new_ascii_value= ascii_letter_value - 1
        #creating the new string
            newstring= newstring + chr(new_ascii_value)
    print(newstring)

    return newstring


def main():
    message=str()
    userchoice=str()
    message=input("Enter text: ")
    userchoice=input("(E)ncrypt or (D)ecrypt? ")

    if userchoice == "E":
        encryptstr(message)
    else:
        decryptstring(message)
    

main()
        
