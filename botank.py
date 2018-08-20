import time,math,random


t_wh = 35 # tank width/height
t_wh_h = 17 # tank width/height half
t_sp = 40 # tank speed
sh_sp = 40 # shoot speed
display = 512, 256 # display x,y
class Botank:
    tanks = [];
    shots = [];
    collisions = [];
    def __init__(self):
        pass
    
    def newTank(self,i):
        available = False
        while available==False:
            available = True
            x=random.randrange(t_wh, display[0]-t_wh)
            y=random.randrange(t_wh, display[1]-t_wh)
            for tank in self.tanks:
                coords=tank.getCoords()
                if coords[0]-t_wh>x and x<coords[0]+t_wh and coords[1]-t_wh>y and y<coords[1]+t_wh:
                    available = False
                    break

        self.tanks.append(Tank(i,x,y,0))

    def getTank(self, i):
        for tank in self.tanks:
            if tank.id==i: return tank
        return False
    def newCommand(self, i, command, arg=None):
        tank=self.getTank(i)
        if tank:
            if command==0:
                tank.stop()
            elif command==1:
                tank.go()
            elif command==2:
                tank.turn(arg)
        return False
            
    def state():
        pass

class Tank:
    """docstring for tank"""
    All = []
    def __init__(self, i, x, y, face):
        self.id = i
        self.x = x
        self.y = y
        self.face = face
        self.time = time.time()
        self.going = False
        Tank.All.append(self)
        #self.collisions = []

    def do(self):
        ttime = time.time()
        dt = ttime-self.time
        if self.going:
            s=dt*t_sp
            temp=self.getNC()
            if temp and temp[0]<s:
            	s-=temp[1]
            	if s<temp[0]: s=temp[0]
            if self.face==0:
                self.y-=s
            elif self.face==1:
                self.x+=s
            elif self.face==2:
                self.y+=s
            elif self.face==3:
                self.x-=s
        self.time = ttime

    def newCommand(self, command, agr=None):

        if command==0:
        	self.going=False
        elif command==1: 
        	self.going=True
        elif command==2:
        	self.face=face

    def getCoords(self):
        self.do()
        return (self.x, self.y)

    def getNC(self):
    	""" the Nearest Collision """
    	temp = []
    	if self.going:
	    	for t in Tank.All:
	    		if t.going:
	    			t.do()
	    			dx = self.x - t.x
	    			dy = self.y - t.y
	    			if self.face==0 and self.y-t.y>t_wh:
	    				if t.face==1:
	    					temp=Tank.auxFunc(temp,dy,dx)
	    				elif t.face==3:
	    					temp=Tank.auxFunc(temp,dy,-dx)
	    				elif t.face==2:
	    					temp.append([dy/2,0])
	    			elif self.face==1 and self.x-t.x>t_wh:
	    				if t.face==0:
	    					temp=Tank.auxFunc(temp,-dx,-dy)
	    				elif t.face==2:
	    					temp=Tank.auxFunc(temp,-dx,dy)
	    				elif t.face==3:
	    					temp.append([-dx/2,0])
	    			elif self.face==2 and t.y-self.y>t_wh:
	    				if t.face==1:
	    					temp=Tank.auxFunc(temp,-dy,dx)
	    				elif t.face==3:
	    					temp=Tank.auxFunc(temp,-dy,-dx)
	    				elif t.face==0:
	    					temp.append([-dy/2,0])
	    			elif self.face==3 and t.x-self.x>t_wh:
	    				if t.face==0:
	    					temp=Tank.auxFunc(temp,dx,-dy)
	    				elif t.face==2:
	    					temp=Tank.auxFunc(temp,dx,dy)
	    				elif t.face==1:
	    					temp.append([dx/2,0])
	    		else:
	    			if self.face==0:
	    				if self.x>t.x-t_wh and self.x<t.x+t_wh and self.y-t.y>t_wh: temp.append([self.y-t.y,0])
	    			elif self.face==1:
	    				if self.y>t.y-t_wh and self.y<t.y+t_wh and self.x-t.x>t_wh: temp.append([self.x-t.x,0])
	    			elif self.face==2:
	    				if self.x>t.x-t_wh and self.x<t.x+t_wh and t.y-self.y>t_wh: temp.append([t.y-self.y,0])
	    			elif self.face==3:
	    				if self.y>t.y-t_wh and self.y<t.y+t_wh and t.x-self.x>t_wh: temp.append([t.x-self.x,0])

		if self.face==0:
		    temp.append([self.y,0])
		elif self.face==1:
		    temp.append([display[0]-self.x,0])
		elif self.face==2:
		    temp.append([display[1]-self.y,0])
		elif self.face==1:
		    temp.append([self.x,0])

	    for t in temp:
			if m==None or m>t[0]:
				m=t[0]
				temp1=t

	    return temp1

    def auxFunc(temp,td1,td2):
        d=td1-td2
        if d>0 and d<t_wh:
            temp.append([td1,d])
        return temp

class Shoot:
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.face = face

class Collision:
    def __init__(self,t1,t2=None,l=0,x=0,y=0):
        self.tank1 = t1
        self.tank2 = t1
        self.x = x
        self.y = y
        self.l = l