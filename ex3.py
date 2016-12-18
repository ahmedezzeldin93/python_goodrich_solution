def prefix_average1(S):
	"""Return list such that for all j, A[j]
	equals the average of S[0], S[1]... S[j]. """
	n = len(S)
	A = [0] * n
	for j in range(n):
		total = 0
		for i in range(j+1):
			total+= S[i]
		A[j] = total / (j+1)
	return A

def prefix_average2(S):
	"""Return list such that for all j, A[j]
	equals the average of S[0], S[1]... S[j]. """
	n = len(S)
	A = [0] * n
	for j in range(n):
		A[j] = sum(S[0:j+1])/(j+1)
	return A

def prefix_average3(S):
	"""Return list such that for all j, A[j]
	equals the average of S[0], S[1]... S[j]. """
	n = len(S)
	A = [0] * n
	total = 0
	for j in range(n):
		total += S[j]
		A[j] = total/(j+1)
	return A

def disjoint1(A,B,C):
	"""Return True if there is no element common 
	to all three lists."""
	for a in A:
		for b in B:
			for c in C:
				if a == b == c:
					return False
	return True

def disjoint(A,B,C):
	"""Return True if there is no element common 
	to all three lists."""
	for a in A:
		for b in B:
			if a == b:
				for c in C:
					if c == b:
						return False
	return True

def unique1(S):
	"""Return True if there are no duplicate elements 
	in sequence S."""
	for j in range(S):
		for k in range(j+1,len(S)):
			if S[j] == S[k]:
				return False
	return True

def unique2(S):
	"""Return True if there are no duplicate elements 
	in sequence S."""
	temp = sorted(S)
	for j in range(1,len(temp)):
		if S[j-1] == S[j]:
			return False
	return True

def unique3(S,start,stop):
	"""Return True if there are no duplicate elements 
	in sequence S. NOT TRUE"""
	if stop - start <= 1: 
		return True
	elif not unique3(S,start,stop-1): 
		return False
	elif not unique3(S,start-1,stop): 
		return False
	else: 
		return S[start] != S[stop-1]

if __name__ == '__main__':
	print(prefix_average1([2,4,5,8,1,5,9,12]))
	print(prefix_average2([2,4,5,8,1,5,9,12]))
	print(prefix_average3([2,4,5,8,1,5,9,12]))
	print(unique3([2,4,5,6,8],0,3))