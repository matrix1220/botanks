import socket,time,_thread,botank

s = socket.socket()
s.bind(("0.0.0.0", 12345))

s.listen(5)

connections = []
bot = botank.Botank()
i=1

def connection():
	c, addr = s.accept()
	bot.newTank(i)
	connection()


_thread.start_new_thread( connection,() )
