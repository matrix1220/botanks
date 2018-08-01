import time,math,random

#tank height/width: 50
#shot going length: 500
#tank max speed:50 1/sec
#shot speed: 250 1/sec
#face rotate max speed: pi radian/sec
#area: 1000, 1000

class Botank:
	tanks = [];
	shots = [];
	def __init__(self):
		pass
	
	def newTank(self,i):
		available = True
		while available==False:
			available = True
			x=random.randrange(50, 950)
			y=random.randrange(50, 950)
			for tank in self.tanks:
				coords=tank.getCoords()
				if coords[0]-75>x and x<coords[0]+75 and coords[1]-75>y and y<coords[1]+75:
					available = False
					break

		self.tanks.append(Tank(i,x,y,0))

	def getTank(self, i):
		for tank in self.tanks:
			if tank.id==i: return tank
		return False
	def newCommand(self, i, command, arg=None):
		if tank=self.getTank(i):
			if command==0:
				tank.stop()
			elif command==1:
				tank.goForward(arg)
			elif command==2:
				tank.goBack(arg)
			elif command==3:
				tank.turnLeft(arg)
			elif command==4:
				tank.turnRight(arg)

			for t in self.tanks:
				tank.verifyRoute(t)
				#if collision=tank.verifyRoute(tt): self.collisions.append(collision)
		return False
			
	def state():
		pass

class Tank:
	"""docstring for tank"""
	def __init__(self, i, x, y, face):
		self.id = i
		self.x = x
		self.y = y
		self.face = face #radian
		self.time = time.time()
		self.action = 0,
		#self.collisions = []

	def stop():
		do()
		self.action=0,

	def goForward(self,speed):
		do()
		self.action=1,speed

	def goBack(self,speed):
		do()
		self.action=2,speed

	def turnLeft(self,angle):
		do()
		self.action=3,angle

	def turnRight(self,angle):
		do()
		self.action=4,angle
	
	def shoot(self):
		pass

	def do():
		if(self.action[0]==0):
			pass
		elif(self.action[0]==1):
			self.x+=math.cos(self.face)*(time.time()-self.time)*self.action[1]
			self.y+=math.sin(self.face)*(time.time()-self.time)*self.action[1]
		elif(self.action[0]==2):
			self.x-=math.cos(self.face)*(time.time()-self.time)*self.action[1]
			self.y-=math.sin(self.face)*(time.time()-self.time)*self.action[1]
		elif(self.action[0]==3):
			self.face-=*(time.time()-self.time)*self.action[1]
		elif(self.action[0]==4):
			self.face+=*(time.time()-self.time)*self.action[1]

		self.time = time.time()

	def getCoords():
		do()
		return (self.x, self.y)

	def verifyRoute(self,t):
		pass

class Shoot:
	def __init__(self, x, y, face):
		self.x = x
		self.y = y
		self.face = face

class Collision:
	def __init__(self):
		pass
		