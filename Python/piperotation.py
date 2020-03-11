r,c = map(int,input().split())

class Pipe:
	def __init__(self,name):
		self.name = name
		self.reqr = 0
		self.reqd = 0
	def __repr__(self):
		return "(" + str(self.reqr) + ', ' + str(self.reqd) + ")"
	def reqright(self,pipe):
		pipe.reqr = 1
	def reqdown(self,pipe):
		pipe.reqd = 1

graph = [list(Pipe(l) for l in input()) for i in range(r)]

flag = True
for i in range(r):
	if not flag:
		break
	for j in range(c):
		p = graph[i][j]
		rr = p.reqr
		rd = p.reqd

		if p.name == 'A':
			if p.reqr or p.reqd:
				flag = False
				break

		if p.name == 'B':
			if p.reqr and p.reqd:
				flag = False
				break
			elif p.reqr and j < c-1:
				p.reqright(graph[i][j+1])
			elif p.reqd and i < r-1:
				p.reqdown(graph[i+1][j])
			else:
				flag = False
				break

		if p.name == 'C':
			if p.reqr and p.reqd:
				continue
			elif not p.reqr and not p.reqd:
				if i < r-1 and j < c-1:
					p.reqright(graph[i][j+1])
					p.reqdown(graph[i+1][j])
				else:
					flag = False
					break
			elif p.reqr and i < r-1:
				p.reqdown(graph[i+1][j])
			elif p.reqd and j < c-1:
				p.reqright(graph[i][j+1])
			else:
				flag = False
				break

		if p.name == 'D':
			if not (p.reqr and p.reqd):
				flag = False
				break
			elif i < r-1 and j < c-1:
				p.reqright(graph[i][j+1])
				p.reqdown(graph[i+1][j])
			else:
				flag = False
				break


print(["Impossible","Possible"][flag])