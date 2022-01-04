#Alternating Split
def decrypt(encrypted_text, n):
    if encrypted_text != None and encrypted_text != "" and n > 0:
        s = ""
        l = len(encrypted_text) - 1
        x = 0
        for i in range(0,len(encrypted_text)):
            if i % 2 == 0:
                s += encrypted_text[int((l+1)/2) + x]
            else:
                s += encrypted_text[(l-l)+x]
                x += 1
        return decrypt(s,n-1)
    else:
        return encrypted_text



def encrypt(text, n):
    s = ""
    if text != None and text != "" and n > 0:
        #Odd numbers loop
        for i in range(1,len(text),2):
            s += text[i]
        #Even numbers loop
        for i in range(0,len(text),2):
            s += text[i]
        return encrypt(s,n-1)
    else:
        return text

#Test
print("Encrypting 012345, twice to 304152:",encrypt("012345",2))
print("Decrypting 20314, thrice to 01234:",decrypt("20314",3))