
Write a Python program to count the most common words in a dictionary. 
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]

words = ['white', 'pink', 'red', 'black', 'white', 'pink', 'black','red', 'white','pink', 'black', 'red', 'pink', 'white', 'black','pink', 'red', 'pink', 'black', 'white']

from collections import Counter
c = Counter(words)
c.most_common(4)
print(c)

#Counter({'pink': 6, 'white': 5, 'black': 5, 'red': 4})


# Write a Python program to find the class wise roll number from a tuple-of-tuples.
Expected Output:
defaultdict(, {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]}) 

from collections import defaultdict
classes = (('V', 1),('VI', 1),('V', 2),('VI', 2),('VI', 3),('VII', 1),)

rollnumber = defaultdict(list)
print(rollnumber)
for class_name, roll_number in classes:
    rollnumber[class_name].append(roll_number)

print(rollnumber)


 Write a Python program to count the number of students of individual class. 
Sample data:
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)
Expected Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})

from collections import Counter

classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)

counter = Counter(class_name for class_name, rollnumber in classes)

print(counter)



Write a Python program to get the unique enumeration values. 
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244




 Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order. 
Expected Output: 
Angola 244
Andorra 376
Algeria 213
Afghanistan 93
Albania 355
In reverse order:
Albania 355
Afghanistan 93
Algeria 213
Andorra 376
Angola 244

from collections import OrderedDict

countries = {'Angola': '244', 'Andorra': '376', 'Algeria': '213', 'Afghanistan': '93', 'Albaniania': '355'}

c = OrderedDict(countries.items())

for i in c:
    print(i, c[i])

print("Countries in reversed order\n")

for i in reversed(c):
    print(i, c[i])

Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
Expected output:
[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]

from collections import defaultdict

class_names = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
c = defaultdict(list)
for i, j in class_names:
    c[i].append(j)
print(c)


 Write a Python program to compare two unordered lists (not sets). 
Expected Output: False

n1 = [ 20, 10, 30, 10, 20, 30 ]
n2 = [ 30, 20, 10, 30, 20, 50 ]

if n1 == n2:
    print("True")
else:
    print("False")




 Write a Python program to create an array contains six integers. Also print all the members of the array. 
Expected Output:
10
20
30
40
50

from array import *
i = array('i', [ 10, 20, 30, 40, 50, 60 ])

for index, value in enumerate(i):
    print(value)



 Write a Python program to get the array size of types unsigned integer and float. 
Expected Output:
4 
4

from array import *
i = array('I', [ 10, 20, 30, 40, 50, 60 ])
j = array('f', [ 10.2, 20.3, 30.3, 40.5, 50.1, 60.3 ])
print(i.itemsize)
print(j.itemsize)

 Write a Python program to get an array buffer information. 
Expected Output:
Array buffer start address in memory and number of elements.
(25855056, 2)

from array import *
i = array('I', [ 10, 20, 30, 40, 50, 60 ])
print(i.buffer_info())


 Write a Python program to get the length of an array. 
Expected Output:
Length of the array is: 
5

from array import *
i = array('I', [ 10, 20, 30, 40, 50, 60 ])
print("Length of the array is: {0}".format(i.buffer_info()[1]))


 Write a Python program to convert an array to an ordinary list with the same items. 
Expected Output:
Original array:
array('b', [1, 2, 3, 4])
Array to list:
[1, 2, 3, 4] 

from array import *
i = array('I', [ 10, 20, 30, 40, 50, 60 ])
print(i.tolist())



 Write a Python program to convert an array to an array of machine values and return the bytes representation. 
Expected Output:
Original array: 
A1: array('i', [1, 2, 3, 4, 5, 6])
Array of bytes: b'010000000200000003000000040000000500000006000000' 

from array import *
i = array('i', [1, 2, 3, 4, 5, 6])
print(i.tobytes())



 Write a Python program to read a string and interpreting the string as an array of machine values. 
Expected Output:
array1: array('i', [7, 8, 9, 10])
Bytes: b'0700000008000000090000000a000000' 
array2: array('i', [7, 8, 9, 10])

 Write a Python program to push three items into the heap and print the items from the heap. 
Expected Output:
('V', 1)
('V', 2)
('V', 3)

from heapq import *
x = []
heappush(x, ('V', 1))
heappush(x, ('V', 2))
heappush(x, ('V', 3))
for item in x:
    print(item)


 Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap. 
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2) 
---------------------- 
The smallest item in the heap:
('V', 1) 
----------------------
Pop the smallest item in the heap:
('V', 2) 
('V', 3)


from heapq import *
x = []
heappush(x, ('V', 1))
heappush(x, ('V', 3))
heappush(x, ('V', 2))
for item in x:
    print(item)
print("Smallest Item: {}".format(x[0]))
heappop(x)
print("Smallest Item in the list")
for item in x:
    print(item)


Write a Python program to push an item on the heap, then pop and return the smallest item from the heap.
Expected Output:
Items in the heap:
('V', 1) 
('V', 3) 
('V', 2) 
----------------------

Using heappushpop push item on the heap and return the smallest item.
('V', 2) 
('V', 3) 
('V', 6)

Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time.
Expected Output:
[10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]

from heapq import *

def heapsort(x):
    print("In : {0}".format(x))
    h = []
    for i in x:
        heappush(h, i)
        print(h)
    return [heappop(h) for j in range(len(h))]

heapsort([10, 90, 20, 80, 50, 20, 100, 70, 40, 50, 60])

 Write a Python program to get the two largest and three smallest items from a dataset. 
Expected Output:
[100, 90]
[10, 20, 20]

from heapq import *
def heapsort(x):
    print("In : {0}".format(x))
    h = []
    for i in x:
        heappush(h, i)
    return [heappop(h) for j in range(len(h))]

sorted = heapsort([10, 90, 20, 80, 50, 20, 100, 70, 40, 50, 60])
print(sorted)
print(sorted[:8:-1])
print(sorted[:3:])


 Write a Python program to locate the left insertion point for a specified value in sorted order. 
Expected Output:
4 
2

from bisect import *
a = [10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
i = 30
y = bisect_left(a, i)
print(y)

 Write a Python program to locate the right insertion point for a specified value in sorted order. 
Expected Output:
3 
2

 Write a Python program to insert items into a list in sorted order. 
Expected Output:
Original List: 
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36] 
Sorted List: 
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]

from bisect import *
a = [14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
print("Original List :{0}".format(a))
i = 30
insort_left(a, i)
print("Inserted List :{0}".format(a))


 a Python program to create a queue and display all the members and size of the queue. 
Expected Output:
Members of the queue:
0 1 2 3 
Size of the queue:
4

from collections import deque
a = 0, 1, 2, 3
y = deque()
for i in a:
    y.append(i)

print("Size of queue :{0}".format(len(y)))
for i in y:
    print(i)

 Write a Python program to find whether a queue is empty or not. 
Expected Output:
True 
False 

from collections import deque
x = deque()
if len(x) == 0:
    print("True")
else:
    print("False")

 Write a Python program to create a FIFO queue. 
Expected Output:
0 1 2 3 

import queue
q = queue.Queue()
for i in range(4):
    q.put(i)

while not q.empty():
    print(q.get())


 Write a Python program to create a LIFO queue. 
Expected Output:
3 2 1 0

import queue
q = queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
