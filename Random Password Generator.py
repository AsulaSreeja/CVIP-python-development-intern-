import random
import string
print("hi,welcome to password generator!")
length=int(input("\n enter the length of the password:"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation
all=lower+upper+digits+symbols
temp=random.sample(all,length)
password="".join(temp)
print(password)
