def linear_sum(S,n):
	"""Return the sum of the first n numbers of sequence S."""
	if n == 0:
		return 0
	else:
		return linear_sum(S,n-1)+S[n-1]

def reverse(S,start,stop):
	"""Reverse element in implicit slice S[start:stop]"""
	if start<stop-1:
		S[start], S[stop-1] = S[stop-1],S[start]
		reverse(S,start+1,stop-1)

if __name__ == '__main__':
	mylist=[1,2,3,4,5]
	print(linear_sum(mylist,5))
	reverse(mylist,0,5)
	print(mylist)