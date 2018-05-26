


1. Write a Python program to print version of python being used

import sys
print(sys.version)


2. Write a Python program to get the Python version you are using.

####################################################################################################################################
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

import datetime
print(str(datetime.datetime(2014, 7, 5, 14, 34, 14)))


4. Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504

import math
r = float(input("Please enter radis:"))
area = r**2 * math.pi
print("Aread of circle is:{0}".format(area))

5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

firstname = input("Please enter first name:")
lastname = input("Please enter last name:")

print(lastname+" "+firstname)

6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')


sample = str(input("Enter comma seperated numbers:"))
sample = sample.split(',')
print("List : {0}".format(sample))
print("Tuple : {0}".format(tuple(sample)))

7. Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java

sample = str(input("Enter file name: "))
print("Output : {0}".format(sample.split('.')[1]))

8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]
print("Color List : {0}".format(color_list))
print("first and laster color from list : {0}".format(color_list[0:4:3]))

9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

import datetime
exam_st_date = (11, 12, 2014)
print("The examination will start from : {0}".format(datetime.date(exam_st_date[2],exam_st_date[1],exam_st_date[0]).strftime("%d/%m/%y")))


10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

n = 5
result = n + n*n + n*n*n
print(result)

11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.

print(abs.__doc__)

12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.

import calendar
year = int(input("Enter the year:"))
month = int(input("Enter the month:"))
print(calendar.month(year, month))



13. Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

import datetime
firstdate = datetime.date(2014, 7, 2)
seconddate = datetime.date(2014, 7, 11)

d = firstdate - seconddate
print(abs(d))

15. Write a Python program to get the volume of a sphere with radius 6.

import math
r= 6.0
V= 4.0/3.0*math.pi* r**3
print("The volume of the sphere is: {0}".format(V))


16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

a  = int(input("First Number:"))
b = 17

if abs(a) > 17:
    print("Output : {0}".format(abs(a - b)) * 2)
else:
    print("Output : {0}".format(abs(a - b)))


17. Write a Python program to test whether a number is within 100 of 1000 or 2000.


18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

def sum(a, b, c):
    total = a + b + c
    if ((a == b) and (a == c) and (b == c)):
        return (total * 3)
    else:
        return total

a = int(input("First Number : "))
b = int(input("Second Number : "))
c = int(input("Third Number : "))

print(sum(a, b, c))

19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def my_string(a):
    string_list = a.split(" ")
    if (string_list[0] == "Is"):
        return a
    else:
        return ("Is"+" "+a)

a = input("Input string: ")
print(my_string(a))

20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def mystring(a, n):
    output = ""
    for i in range(n):
        output = output + a
    return output

print(mystring("Hello", 5))



21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def even_or_odd(a):
    output = a % 2
    if output == 0:
        print("This is EVEN number")
    else:
        print("This is ODD  number")

a = int(input("Please enter number to find it is even or odd : "))
even_or_odd(a)

22. Write a Python program to count the number 4 in a given list.

def count_numbers(a):
    counter = 0
    for i in range(len(a)):
        if (int(a[i]) == 4):
            counter = counter + 1
    return counter

input_data = input("Input List :")
a = input_data.split(',')
print("The number 4 is repeated {0} times".format(count_numbers(a)))


23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def copies(mystring, n):
    if len(mystring) > 2:
        output = ""
        for i in range(n):
            output = output + mystring[:2]
        return output
    else:
        return mystring

a = input("Input string :")
copies(a, 4)

24. Write a Python program to test whether a passed letter is a vowel or not.

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))

25. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

input_list = [ 1, 5, 8, 3 ]
input_value = int(input("Enter the value:"))
print("Does {0} exists in {1} ? {2}".format(input_value, input_list, input_value in input_list))



26. Write a Python program to create a histogram from a given list of integers.


27. Write a Python program to concatenate all elements in a list into a string and return it.


28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
Sample numbers list :

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]


29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}


30. Write a Python program that will accept the base and height of a triangle and compute the area.


31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.


32. Write a Python program to get the least common multiple (LCM) of two positive integers.


33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.


34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.


36. Write a Python program to add two objects if both objects are an integer type.


37. Write a Python program to display your details like name, age, address in three different lines.


38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49


39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79


40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).


41. Write a Python program to check whether a file exists.


42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.


43. Write a Python program to get OS name, platform and release information.


44. Write a Python program to locate Python site-packages.


45. Write a python program to call an external command in Python.


46. Write a python program to get the path and name of the file that is currently executing.


47. Write a Python program to find out the number of CPUs using.


48. Write a Python program to parse a string to Float or Integer.


49. Write a Python program to list all files in a directory in Python.


50. Write a Python program to print without newline or space.


51. Write a Python program to determine profiling of Python programs.
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.


52. Write a Python program to print to stderr.


53. Write a python program to access environment variables.


54. Write a Python program to get the current username


55. Write a Python to find local IP addresses using Python's stdlib


56. Write a Python program to get height and width of the console window.


57. Write a program to get execution time for a Python method.


58. Write a python program to sum of the first n positive integers.


59. Write a Python program to convert height (in feet and inches) to centimeters.


60. Write a Python program to calculate the hypotenuse of a right angled triangle.


61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.


62. Write a Python program to convert all units of time into seconds.


63. Write a Python program to get an absolute file path.


64. Write a Python program to get file creation and modification date/times.


65. Write a Python program to convert seconds to day, hour, minutes and seconds.


66. Write a Python program to calculate body mass index.


67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.


68. Write a Python program to calculate the sum of the digits in an integer.


69. Write a Python program to sort three integers without using conditional statements and loops.


70. Write a Python program to sort files by date.


71. Write a Python program to get a directory listing, sorted by creation date.


72. Write a Python program to get the details of math module.


73. Write a Python program to calculate midpoints of a line.


74. Write a Python program to hash a word.


75. Write a Python program to get the copyright information.


76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.


77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.


78. Write a Python program to find the available built-in modules.


79. Write a Python program to get the size of an object in bytes.


80. Write a Python program to get the current value of the recursion limit.


81. Write a Python program to concatenate N strings.


82. Write a Python program to calculate the sum over a container.


83. Write a Python program to test if a certain number is greater than all numbers of a list.


84. Write a Python program to count the number occurrence of a specific character in a string.


85. Write a Python program to check if a file path is a file or a directory.


86. Write a Python program to get the ASCII value of a character.


87. Write a Python program to get the size of a file.


88. Given variables x=30 and y=20, write a Python program to print t "30+20=50".


89. Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.


90. Write a Python program to create a copy of its own source code.


91. Write a Python program to swap two variables.


92. Write a Python program to define a string containing special characters in various forms.


93. Write a Python program to get the identity of an object.


94. Write a Python program to convert a byte string to a list of integers.


95. Write a Python program to check if a string is numeric.


96. Write a Python program to print the current call stack.


97. Write a Python program to list the special variables used within the language.


98. Write a Python program to get the system time.

Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.


99. Write a Python program to clear the screen or terminal.


100. Write a Python program to get the name of the host on which the routine is running.


101. Write a Python program to access and print a URL's content to the console.


102. Write a Python program to get system command output.


103. Write a Python program to extract the filename from a given path.


104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.
Note: Availability: Unix.


105. Write a Python program to get the users environment.


106. Write a Python program to divide a path on the extension separator.


107. Write a Python program to retrieve file properties.


108. Write a Python program to find path refers to a file or directory when you encounter a path name.


109. Write a Python program to check if a number is positive, negative or zero.


110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.


111. Write a Python program to make file lists from current directory using a wildcard.


112. Write a Python program to remove the first item from a specified list.


113. Write a Python program to input a number, if it is not a number generate an error message.


114. Write a Python program to filter the positive numbers from a list.


115. Write a Python program to compute the product of a list of integers (without using for loop).


116. Write a Python program to print Unicode characters.


117. Write a Python program to prove that two string variables of same value point same memory location.


118. Write a Python program to create a bytearray from a list.


119. Write a Python program to display a floating number in specified numbers.


120. Write a Python program to format a specified string to limit the number of characters to 6.


121. Write a Python program to determine if variable is defined or not.


122. Write a Python program to empty a variable without destroying it.

Sample data: n=20
d = {"x":200}
Expected Output : 0
{}



123. Write a Python program to determine the largest and smallest integers, longs, floats.


124. Write a Python program to check if multiple variables have the same value.


125. Write a Python program to sum of all counts in a collections?


126. Write a Python program to get the actual module object for a given object.


127. Write a Python program to check if an integer fits in 64 bits.


128. Write a Python program to check if lowercase letters exist in a string.


129. Write a Python program to add leading zeroes to a string.


130. Write a Python program to use double quotes to display strings.


131. Write a Python program to split a variable length string into variables.


132. Write a Python program to list home directory without absolute path.


133. Write a Python program to calculate the time runs (difference between start and current time) of a program.


134. Write a Python program to input two integers in a single line.


135. Write a Python program to print a variable without spaces between values.
Sample value : x =30
Expected output : Value of x is "30"


136. Write a Python program to find files and skip directories of a given directory.


137. Write a Python program to extract single key-value pair of a dictionary in variables.


138. Write a Python program to convert true to 1 and false to 0.


139. Write a Python program to valid a IP address.


140. Write a Python program to convert an integer to binary keep leading zeros.
Sample data : 50
Expected output : 00001100, 0000001100


141. Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04


142. Write a Python program to find the operating system name, platform and platform release date.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic


143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.


144. Write a Python program to check if variable is of integer or string.


145. Write a Python program to find the operating system name, platform and platform release date.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic


146. Write a Python program to find the location of Python module sources.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic


147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.


148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
Note: Do not use built-in functions.


149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.


150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.