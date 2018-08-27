def descending(l):

	if l:
		t = l[0]
		for i in l[1:]:
			if i > t:
				return False
			t = i

	return True

def transpose(m):

	return [list(x) for x in zip(*m)]

def valley(l):

	m = min(l)

	d = 1

	if l[0] != m and l[-1] != m:
		
		t = l[0]

		for i in l[1:]:

			if d and i >= t:
				return False

			if not d and i <= t:
				return False

			if i == m:
				d = 0

			t = i 

		return True
	else:
		return False


def func(arr):

	count=0
	count2=0
	f1=0;
	for i in range(1,len(arr)):

		if(arr[i]<arr[i-1]):

			count += 1
			continue

		if(arr[i]>arr[i-1]):
			count2 += 1
			continue
		else:
			f1=1
			break

	if(count>1 and count2>1 and f1==0):
		return True
	else:
		return False


