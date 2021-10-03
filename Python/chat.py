import socket
import threading
import os


os.system("tput setaf 3")
print("\t"+72*"=")
print("\t\t\t\tWelcome To The Chat Bot")
print("\t"+72*"=")
os.system("tput setaf 7")

# Server Credential
os.system("tput setaf 5")
ip = input("\t\t\tPlease Provide Server IP : ")
port = int(input("\t\t\tPlease Provide the Server Port :"))
os.system("tput setaf 7")

# Your Credentials
os.system("tput setaf 5")
ips= input("\t\t\tPlease Provide Your IP : ")
ports=  int(input("\t\t\tPlease Provide Your Port :"))
os.system("tput setaf 7")

#Binding the Port & IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (ip, port) )
    

def a():
    while True:
        x =  input("\nYou : ")
        s.sendto(x.encode(), (ips, ports))
        if x == "exit" or x == "quit":
            os._exit(1)

def b():
    while True:
        y = s.recvfrom(10)
        cip = y[1][0]
        data = y[0].decode()
        print(f"\nClient@{cip} :",data)
        if data == "quit" or data == "exit":
            os._exit(1)

x1 = threading.Thread(target=a)
x2 = threading.Thread(target=b)

x1.start()
x2start()
