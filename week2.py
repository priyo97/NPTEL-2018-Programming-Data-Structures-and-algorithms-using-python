def matched(s):

	count = 0

	for i in s:
		if count < 0:
			return False
		elif i == "(":
			count += 1
		elif i == ")":
			count -= 1

	return (count == 0)

def intreverse(n):
	'''
	sum = 0
	while n:
		sum = sum*10 + n%10
		n = n//10
	return sum
	'''

	n_str = str(n)
	return n_str[::-1]

def sumprimes(l):

	sum1 = 0
	for i in l:
		if i > 1 and isprime(i):
			sum1 += i

	return sum1

def isprime(n):

	for i in range(2,n):
		if n%i == 0:
			return False

	return True