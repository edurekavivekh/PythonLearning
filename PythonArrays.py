#1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
from array import *
import sys
myarray = array('i',[3, 4, 8, 34, 3])
print("Here is my array: {0}".format(myarray))

#for i in range(0, len(myarray)):
#    print(myarray[i])
for index, value in enumerate(myarray):
    print(myarray[index])
    # print(index, value)
#######################################################################################################################################
#2. Write a Python program to append a new item to the end of the array.

a = array('i', [45, 56, 6, 7, 22])
print("Original array:{0}".format(a))
a.append(100)
print("Modified Array, post item append:{0}".format(a))
print(a)
#######################################################################################################################################
#3. Write a Python program to reverse the order of the items in the array.

engineers = [ 'Uma', 'Sohil', 'Dilip', 'Vivek', 'Satya' ]
print("Original array:{0}".format(engineers))

#engineers = engineers[::-1]
engineers.reverse()
print("ReverseOrder Array:{0}".format(engineers))

#######################################################################################################################################
#4. Write a Python program to get the length in bytes of one array item in the internal representation.


a = array('i', [ 200, 5, 8, 4])
print(sys.getsizeof(a[1]))

#######################################################################################################################################
#5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.

a = array('i', [ 2, 5, 2, 7, 4])
print("Current memory address & length of buffer:{0}".format(a.buffer_info()))
print("Size of single item in bytes:{0}".format(a.itemsize))
print("Size of memory buffer in bytes:{0}".format(a.buffer_info()[1] * a.itemsize))

#######################################################################################################################################
#6. Write a Python program to get the number of occurrences of a specified element in an array.
a = array('i', [ 2, 2, 4, 5, 5, 5, 8, 8, 2 ])

for i in range(0, len(a)):
    print("{0} is repeated {1} times in an array".format(a[i], a.count(a[i])))

'''count = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        if a[i] == a[j]:
            count = count + 1
           a.
    print("{0} is repeated {1} number of times in an array".format(a[i], count))
    count = 0
    '''
#######################################################################################################################################
#7. Write a Python program to append items from iterrable to the end of the array.

a = array('i', [ 2, 1, 4, 2, 6, 8 ])
print(a)
a.extend(a)
print("Extended Array: {0}".format(a))

#######################################################################################################################################
#8. Write a Python program to convert an array to an array of machine values and return the bytes representation.

x = array('b', [ 97, 98, 99, 100, 101 ])
print(x.tobytes())
# b'\x02\x00\x00\x00"\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00\x08\x00\x00\x00'

#######################################################################################################################################
#9. Write a Python program to append items from a specified list.

X = array('i', [ 3, 4, 5, 6, 7 ])
Y = [ 11, 12, 13, 14, 15, 16 ]
X.fromlist(Y)
print(X)

#######################################################################################################################################
10.Write a Python program to insert a new item before the second element in an existing array

p = array('i', [2, 3, 4, 5, 6])
X = 299
p.insert(1, X)
print(p)

#######################################################################################################################################

11. Write a Python program to remove a specified item using the index from an array.
p = array('i', [2, 3, 4, 5, 6])
print(p.pop(2))
print(p)

#######################################################################################################################################
12. Write a Python program to remove the first occurrence of a specified element from an array.
p = array('i', [2, 3, 4, 5, 6])
p.remove(5)
print(p)

13. Write a Python program to convert an array to an ordinary list with the same items.

p = array('i', [2, 3, 4, 5, 6])
print(p.tolist())

