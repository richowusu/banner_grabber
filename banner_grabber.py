import socket

#Taking inputs
ip_addr = input("Enter the IP address you want to enumerate: ")
Ports = input("Enter the ports you want to enumerate: ")

#Splitting the ports entered into single port removing the commas
for Port in Ports:
 Port = Ports.split(",")

#Grabs information from target machine 
for i in range(0,4):
 client = socket.socket()
 client.connect((ip_addr, int(Port[i])))
 answer = client.recv(4096)
 print(answer)