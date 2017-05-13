#! /usr/bin/env python3.5
#  -*- coding = utf - 8 -*-
import random
import copy
op1=[[1,2,3],
	 [4,5,6],
	 [7,8,0]
]
op2=[[1,2,3],
	 [8,0,4],
	 [7,6,5]
]
class ep:
	def __init__(self,ip,op,parent=None,dirF=None,depth=1):
		self.ip=ip
		self.dir=['up','right','down','left']
		self.parent=parent
		self.depth=depth
		self.op=op
		if dirF:
			self.dir.remove(dirF)
		d1=[]
		d2=[]
		for j in range(1,9):
			for i in range(len(self.ip)):
				if j in self.ip[i]:
					d1.append([i,ip[i].index(j)])
				if j in self.op[i]:
					d2.append([i,op[i].index(j)])
		a=0
		for k in range(8):
			a=abs(d1[k][0]-d2[k][0])+abs(d1[k][1]-d2[k][1])+a
		self.zy=a+self.depth
	def findzero(self,i):
		for x in range(3):
			for y in range(3):
				if self.ip[x][y]==i:
					return x,y

	def findpath(self):
		if not self.dir:
			return []
		dip=[]
		x,y=self.findzero(0)
		if 'down' in self.dir and x<2:
			a=copy.deepcopy(self.ip)
			temp=copy.deepcopy(a)
			a[x][y]=a[x+1][y]
			a[x+1][y]=temp[x][y]
			nc=ep(a,op=self.op,dirF='up',parent=self,depth=self.depth+1)
			dip.append(nc)
		if 'up' in self.dir and x>0:
			a=copy.deepcopy(self.ip)
			temp=copy.deepcopy(a)
			a[x][y]=a[x-1][y]
			a[x-1][y]=temp[x][y]
			nc=ep(a,op=self.op,dirF='down',parent=self,depth=self.depth+1)
			dip.append(nc)
		if 'left' in self.dir and y>0:
			a=copy.deepcopy(self.ip)
			temp=copy.deepcopy(a)
			a[x][y]=a[x][y-1]
			a[x][y-1]=temp[x][y]
			nc=ep(a,op=self.op,dirF='right',parent=self,depth=self.depth+1)
			dip.append(nc)
		if 'right' in self.dir and y<2:
			a=copy.deepcopy(self.ip)
			temp=copy.deepcopy(a)
			a[x][y]=a[x][y+1]
			a[x][y+1]=temp[x][y]
			nc=ep(a,op=self.op,dirF='left',parent=self,depth=self.depth+1)
			dip.append(nc)
		return dip
	def show(self):
		for i in range(3):
			for j in range(3):
				print(self.ip[i][j],end='  ')
			print('\n')
		print('next:')
		return

				
	def plana(self):
		opentable=[]
		closetable=[]
		opentable.append(self)
		count=0
		while len(opentable)>0:
			temp=opentable.pop(0)
			closetable.append(temp)
			#print(temp.ip)
			#print(temp.zy)
			#print(temp.depth)
			temp1=temp.findpath()
			temp2=[]
			path=[]
			for s in temp1:
				if s.ip==s.op:
					while s.parent and s.parent != originals:
						path.append(s.parent)
						s=s.parent
					path.reverse()
					return path,count+1
				if s not in closetable:
					temp2.append(s)
			opentable.extend(temp2)
			opentable.sort(key=lambda x:x.zy)
			count=count+1
		else:
			return None,None

def ini():
	ip=[]
	temp=[]
	while len(temp)<9: 
		a=round(random.uniform(0,0.8)*10)
		if a not in temp:
			temp.append(a)
	ip.append(temp[0:3])
	ip.append(temp[3:6])
	ip.append(temp[6:9])
	return ip,temp
def pdj(ip):
	ct=0
	for i in range(9):
		for j in range(i):
			if ip[i]<ip[j]:
				ct=ct+1
	if ct%2==0:
		return op1
	else:
		return op2
if __name__=='__main__':

    ip=ini()
    op=pdj(ip[1])
    originals=ep(ip=ip[0],op=op)
    s=ep(ip=originals.ip,op=op)
    paths, count = s.plana()
    print("\n\nstart:\n\n")
    if paths:
        for path in paths:
            path.show()

    print('oringinal state:',originals.ip)
    print('result:',op)
    print("step: %d" % path.depth)
