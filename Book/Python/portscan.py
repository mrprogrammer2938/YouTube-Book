"""
How To Write PortScanner with Python


Port Scanner With Python

File Saved To: https://github.com/mrprogrammer2938/YouTube/book/Python

Ok Lets Go to Write Port Scanner With Ruby


"""
import socket # import socket python library
import os  # import os library for clear screen
os.system("cls") # clear screen
host = input("\nEnter Host: ") # host Input
print("\n") # Next Line
ports = [21,22,23,80,111,443] # Ports

for port in ports:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    check = s.connect_ex((host,port)) 
    if check == 0:
        print(f"Port: {port} Open!")
    else:
        print(f"Port: {port} Filter!")
"""
if check : 0 = Open

else: Filter 
"""
