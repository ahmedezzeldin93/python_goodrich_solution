'''
This is file contain exercises 1 for
data structures and algorithms in python
All Exercises Done by github@ahmedezzeldin93
'''

#R-1.1
def is_multiple(n,m):
    return True if n%m == 0 else False

#R-1.2
def is_even(k):
    return not k & 1

#R-1.3
def minmax(data):
    minimum, maximum = 99999999,0
    for i in data:
        if i > maximum:
            maximum = i
            continue
        if i < minimum:
            minimum = i
            continue
    return minimum, maximum

#R-1.4 #R-1.5
def sum_of_squares(n):
    arr = [i**2 for i in range(1,n)]
    return sum(arr)

#R-1.6 #R-1.7
def sum_of_squares_of_odds(n):
    arr = [i**2 for i in range(1,n) if i%2 != 0]
    return sum(arr)

#R-1.12
import random
def mychoice_random(arr):
    choice = random.randrange(0,len(arr),1)
    return arr[choice]

#C-1.13
def reverse_list(arr):
    reversed_list = []
    i = len(arr)-1
    while i >= 0:
        reversed_list.append(arr[i])
        i = i - 1
    return reversed_list,

#C-1.14
def detect_odd_product(arr):
    i = 0
    while i < len(arr)-1:
        if (arr[i] * arr[i+1])%2 != 0:
            return True
        i+=1
    return False

#C-1.15
def element_in_list(element,arr):
    for i in arr:
        if i == element:
            return True
    return False

def distinct_list(arr):
    mylist = []
    for i in arr:
        if element_in_list(i,mylist):
            return False
        else:
            mylist.append(i)
    return True

#C-1.20
def myshuffle(data):
    arr= []
    k = 0
    length = len(data)
    while k < length:
        i = random.randint(0,length-k-1)
        arr.append(data[i])
        del data[i]
        k +=1
    return arr

#C.1.22
def dot_product(a,b):
    c = []
    i = 0
    while i < len(a):
        c.append(a[i] * b[i])
        i+=1
    return c

#C-1.28
def norm(v, p=2):
    arr = [i**p for i in v]
    summ = sum(arr)
    return summ ** (1./float(p))

if __name__ == '__main__':
    #R-1.1
    print(is_multiple(10,5))
    #R-1.2
    print(is_even(22))
    #R-1.3
    print(minmax([4,4,6,7,8,1,10]))
    #R-1.4 R-1.5
    print(sum_of_squares(5))
    #R-1.6 R-1.7
    print(sum_of_squares_of_odds(10))
    print([2**i for i in range(9)])
    #R-1.12
    print(mychoice_random([3,4,5,5,6,7,8,8,9,12,19]))
    #C-1.13
    print(reverse_list([1,2,3,4,5,6,7,8]))
    #C-1.14
    print(detect_odd_product([1,2,3,4,5,6,3,7,8]))
    #C-1.15
    print(distinct_list([1,2,3,4,5,6,6]))
    #C-1.18
    print([i*(i+1) for i in range(10)])
    #C-1.19
    print([chr(x) for x in range(97,123)])
    #C-1.28
    print(norm([1,2,3,4,5],3))
    #C-1.20
    print(myshuffle([1,2,3,4,5]))
    #C-1.22
    print(dot_product([1,2,3,4],[5,6,7,8]))
