import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 2237

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if len(data) == 35:
        software = data[16:20].decode()
        sw_version = data[28:].decode()
        res = f'Software: {software} Version: {sw_version}'
        print("35",res)
    
    elif len(data) == 69:
        software = data[16:20].decode()
        callee, caller, report = data[50:].decode().split(" ")
        print("69", software, callee, caller, report)

    elif len(data) == 106:
        print("Len:",len(data))
        #print(data[0], data[1], data[2], data[3])
        #print(data[4:15].decode())
        software = data[16:21].decode()
        #print(data[22:23].decode())
        #print(data[23])
        mesg = str.encode(data[29:64].decode()) 
        print(mesg)
        print("\n")
    """if len(data) >= 69:
        #for i in range(len(data)):
        #    print(i, data[i])
        #software = data[16:20].decode()
        #db = data[20:22].decode()
        #freq = data[23:30].decode()
        #time = data[20:27].decode()
        #print(data[20:].decode())
        try:
            print(data)
            #mesg = data[50:].decode()
            #print(mesg)
        except:
            pass
    else:
        print(50*"*")
"""
 