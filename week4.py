def orangecap(d):

	l = {}

	for k in d:
		for j in d[k]:
			l[j] = l.get(j,0) + d[k][j]

	idx = max(l,key=lambda x:l[x])

	return (idx,l[idx])


def addpoly(p1,p2):

	m = max(p1[0][1],p2[0][1])

	d1 = {y:x for x,y in p1}
	d2 = {y:x for x,y in p2}
	 
	l = []

	for i in range(m,-1,-1):
		
		if i in d1 and i in d2:
			
			c = d1[i] + d2[i]

			if c:
				l.append((c,i))

		elif i in d1:
		
			l.append((d1[i],i))
		elif i in d2:
		
			l.append((d2[i],i))

	return l 



def multpoly(p1,p2):

	l = []

	for i in p1:
		t = [( x[0]*i[0], x[1]+i[1] ) for x in p2 ]
		l.append(t)


	i = l[0]

	for j in l[1:]:

		i = addpoly(i,j)

	return i 


