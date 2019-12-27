import socket,time,_thread 



def connection(i):
	time.sleep(4)
	i+=1
	print(i)
	if i>10:
		exit()
	_thread.start_new_thread( connection,(i,) )
	s = socket.socket()
	s.connect(("127.0.0.1", 12345))
	while 1:
		print(s.recv(1))
	s.close()

connection(0)