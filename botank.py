import time,math,random

t_wh = 35 # tank width/height
t_wh_h = 17 # tank width/height half
t_sp = 40 # tank speed px/s
sh_sp = 40 # shoot speed px/s
display = 512, 256 # display x,y

class Botank:
	
	def newTank(i):
		available = False
		while available==False:
			x=random.randrange(t_wh, display[0]-t_wh)
			y=random.randrange(t_wh, display[1]-t_wh)
			Botank.render()
			available = Botank.isAvailable(x,y)

		return Tank(i,x,y,0)

	def isAvailable(x,y):
		available = True
		for tank in Tank.All:
			if tank.pos.x-t_wh>x and x<tank.pos.x+t_wh and tank.pos.y-t_wh>y and y<tank.pos.y+t_wh:
				available = False
				break
		return available

	def getTank(i): # trouble
		for tank in Tank.All:
			if tank.id==i: return tank
		return False

	def newCommand(i, command, arg=None):
		tank=self.getTank(i)
		if tank:
			tank.newCommand(command,arg)
		return False

	def render():
		ttime=time.time()
		for t in Tank.All:
			Botank.renderTank(t,ttime)

	def renderTank(t,ttime):
		colls=t.findCollisions()
		if not colls:
			t.sdo(t.do(ttime))


class Tank:
	"""docstring for tank"""
	All = []
	def __init__(self, i, x, y, face):
		self.id = i
		self.pos = Point(x,y)
		self.face = Ray(self.pos, angle=face)
		self.btime = time.time() # time of last render
		self.going = False
		self.s = 0 # the displacement of last render
		Tank.All.append(self)

	def findCollisions(self):
		for t in Tank.All:
			if t!=self:
				temp = intersection(self,t)
				if temp: yield temp

	def do(self,ttime): # gives how much to move
		if self.going:
			return math.floor((ttime-self.btime)*t_sp-self.s)
		else:
			return 0

	def sdo(self,s): #moves tank
		if self.going:
			self.pos.translate(sin(self.face.angle)*s,cos(self.face.angle)*s)


	def newCommand(self, command, arg=None):
		ttime=time.time()
		Botank.renderTank(self,ttime)
		self.s = 0
		self.btime = ttime
		if command==0:
			self.going=False
		elif command==1: 
			self.going=True
		elif command==2:
			if arg == 0:
				self.face.rotate(pi)
				print("hi")
			elif arg == 1:
				self.face.rotate(pi)

	def getCoords(self):
		ttime=time.time()
		Botank.renderTank(self,ttime)
		return (self.pos.x-t_wh_h, self.pos.x-t_wh_h)

	# def N2G(N):
	# 	if N==0:
	# 		return 90
	# 	elif N==1
	# 		return 0
	# 	elif N==2
	# 		return 270
	# 	elif N==3
	# 		return 180