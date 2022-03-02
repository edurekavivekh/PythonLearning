1. Write a Python script to sort (ascending and descending) a dictionary by value.


import operator
age = { 'a' : 20, 'b' : 5, 'c' : 60, 'd' : 50 }
print("Its sorted dictionary items : {0}".format(sorted(age.items(), key = operator.itemgetter(1))))
print("Its reverse sorted dictionary items : {0}".format(sorted(age.items(), key = operator.itemgetter(1), reverse = True)))


2. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

a = {0: 10, 1: 20}
a.update({2: 30})
print(a)

3. Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dictT = {}

dictT.update(dic1)
dictT.update(dic2)
dictT.update(dic3)

print(dictT)

from itertools import chain
dictT = {}
dictT = dict(chain.from_iterable(d.iteritems() for d in (dict1, dict2, dict3))

4. Write a Python script to check if a given key already exists in a dictionary.

def iskey(key, data):
    if key in data:
        return True
    else:
        return False


iskey(2, dictT)


5. Write a Python program to iterate over dictionaries using for loops.

dictT = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for key in dictT:
    print(dictT[key])
print(dictT.items())

6.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = 5
a = {}
for key in range(n+1):
    a[key] = key*key

print(a)


7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

n = 15
a = {}
for key in range(1,n+1):
    a[key] = key*key

print(a)


8. Write a Python script to merge two Python dictionaries.

a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
b = {8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
c = {}
c.update(a)
c.update(b)
print(c)

9. Write a Python program to iterate over dictionaries using for loops.


10. Write a Python program to sum all the items in a dictionary.

a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

print(sum(a.values()))

11. Write a Python program to multiply all the items in a dictionary.

a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
m_out = 1
for key in a:
    m_out = m_out * a[key]
    print(a[key])
print(m_out)

12. Write a Python program to remove a key from a dictionary.

def deldictkey(key, data):
    print("Data In :{0}".format(data))
    del data[key]
    return data
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

print(deldictkey(4, data))


13. Write a Python program to map two lists into a dictionary.

list1 = [ 'a', 'b', 'c', 'd', 'e', 'f']
list2 = [ '1', '2', '3', '4', '5', '6']
dictT = dict()

dictT = dict(zip(list1, list2))

print(dictT)

14. Write a Python program to sort a dictionary by key.

numbers = {13: 169, 4: 16, 6: 36, 10: 100, 7: 49, 2: 4, 8: 64, 3: 9, 9: 81, 11: 121, 12: 144, 14: 196, 5: 25, 15: 225, 1: 1}
keys = []
values = []
print("Input Dictionary :{0}".format(numbers))
for key in sorted(numbers):
    keys.append(key)
    values.append(numbers[key])
print(dict(zip(keys, values)))


15. Write a Python program to get the maximum and minimum value in a dictionary.

numbers = {13: 169, 4: 16, 6: 36, 10: 100, 7: 49, 2: 4, 8: 64, 3: 9, 9: 81, 11: 121, 12: 144, 14: 196, 5: 25, 15: 225, 1: 1}

print("Minimum value in dictionary is : {0}".format(min(numbers.values())))
print("Maximum value in dictionary is : {0}".format(max(numbers.values())))

16.Write a Python program to get a dictionary from an object's fields.


class objectClass(object):
    def __init__(self):
        self.a = 234
        self.b = 1999

    def process(self):
        pass


myobj = objectClass()

print(myobj.__dict__)

17. Write a Python program to remove duplicates from Dictionary.

mydict = {'a' : '255', 'b' : '255', 'c' : '34', 'd' : '14', 'e' : '34'}
out_dict = {}
for key, value in mydict.items():
    if value not in out_dict.values():
        out_dict[key] = value

print(out_dict)

18. Write a Python program to check a dictionary is empty or not.


19. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


20. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd


22. Write a Python program to find the highest 3 values in a dictionary.


23. Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})


24. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


25. Write a Python program to print a dictionary in table format.


26. Write a Python program to count the values associated with key in a dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True


27. Write a Python program to convert a list into a nested dictionary of keys.


28. Write a Python program to sort a list alphabetically in a dictionary.


29. Write a Python program to remove spaces from dictionary keys.


30. Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3


31. Write a Python program to get the key, value and item in a dictionary.


32. Write a Python program to print a dictionary line by line.


33. Write a Python program to check multiple keys exists in a dictionary.


34. Write a Python program to count number of items in a dictionary value that is a list.


35. Write a Python program to sort Counter by value.
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]


36. Write a Python program to create a dictionary from two lists without losing duplicate values.
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})


37. Write a Python program to replace dictionary values with their sum.


38. Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y