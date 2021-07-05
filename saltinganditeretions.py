import hashlib
import os
str = input("Enter any string : ")
salt = os.urandom(32)
str = (salt.hex())+str+(salt.hex())
iteretion=5
print("The string after salting : "+str)
while iteretion > 0:
    salt = os.urandom(32)
    str=(salt.hex())+(salt.hex())+str+(salt.hex())+(salt.hex())
    iteretion-=1
print("The string after salting and iteretion : "+str)
h1=hashlib.md5(str.encode())
h2=hashlib.sha256(str.encode())
h3=hashlib.sha512(str.encode())
final1=(h1.hexdigest())
final2=(h2.hexdigest())
final3=(h3.hexdigest())
print("The converted hash of your string using md5 : " +final1)
print("The converted hash of your string using sha256 : " +final2)
print("The converted hash of your string using sha512 : " +final3)

