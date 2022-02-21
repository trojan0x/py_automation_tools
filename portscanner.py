import socket
target = "127.0.0.1"

def scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    
    except:
        return False
         
for port in range(1, 8050):
    result = scanner(port)
    if result:
        print("port {} is open".format(port))
        break
    else:
        print("Port {} is closed".format(port))
