import hashlib
str = input("Enter any string :")
h1=hashlib.md5(str.encode())
final=(h1.hexdigest())
print("The converted hash of your sting is :" +final)
