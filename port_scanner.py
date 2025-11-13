from socket import *

# دریافت آیپی
ip = input("Enter IP : ")
# دریافت پورت
port = int(input("Enter PORT : "))

s = socket(AF_INET , SOCK_STREAM)
r = s.connect_ex((ip,port))

if r == 0 :
    print(f"PORT {port} is open")
else :
    print(f"PORT {port} is close")

s.close()
