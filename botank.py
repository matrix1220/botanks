import time,math

#tank radius: 50
#shot going length: 500
#tank max speed:50 1/sec
#shot speed: 250 1/sec
#face rotate max speed: pi radian/sec
#target rotate max speed: 2*pi radian/sec
#area: 1000, 1000

class botank:
	"""docstring for botank"""
	#tanks
	#shots
	def __init__(self):
		pass
	
	def newTank():
		pass

	def newCommand():
		pass

	def state():
		pass

class tank:
	"""docstring for tank"""
	def __init__(self, x, y, face):
		self.x = x
		self.y = y
		self.face = face
		self.target = 0
		self.time = time.time()
		self.action = 0,

	def stop():
		do()
		self.action=0,
		self.time = time.time()

	def goForward(self,speed):
		do()
		self.action=1,speed
		self.time = time.time()

	def goBack(self,speed):
		do()
		self.action=2,speed
		self.time = time.time()

	def turnLeft(self,angle):
		do()
		self.action=3,angle
		self.time = time.time()

	def turnRight(self,angle):
		do()
		self.action=4,angle
		self.time = time.time()

	def turnTargetLeft(self,angle):
		do()
		self.action=5,angle
		self.time = time.time()

	def turnTargetRight(self,angle):
		do()
		self.action=6,angle
		self.time = time.time()
	
	def shoot(self):
		pass

	def do():
		if(self.action[0]==0):
			pass
		elif(self.action[0]==1):
			self.x+=math.cos(self.face)*(time.time()-self.time)*self.action[0]
			self.y+=math.sin(self.face)*(time.time()-self.time)*self.action[0]
		elif(self.action[0]==2):
			self.x-=math.cos(self.face)*(time.time()-self.time)*self.action[0]
			self.y-=math.sin(self.face)*(time.time()-self.time)*self.action[0]
		elif(self.action[0]==3):
			self.face-=*(time.time()-self.time)*self.action[0]
		elif(self.action[0]==4):
			self.face+=*(time.time()-self.time)*self.action[0]
		elif(self.action[0]==5):
			self.target-=*(time.time()-self.time)*self.action[0]
		elif(self.action[0]==6):
			self.target+=*(time.time()-self.time)*self.action[0]

	def getCoords():
		return (self.x, self.y)
class shoot:
	"""docstring for shoot"""
	def __init__(self, x, y, face):
		self.x = x
		self.y = y
		self.face = face

