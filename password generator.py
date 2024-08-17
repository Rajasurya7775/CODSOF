import random
import string

def password(l):
    char=string.ascii_letters
    password="".join(random.choice(char) for i in range(l))
    return password
    
len=int(input("Enter the password length:"))
print("Password is :",password(len))