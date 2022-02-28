# 1
# design and implement python program to accept 3 digits from user and print all possible combinations from digits

first = int(input("Enter number : "))
second = int(input("Enter number : "))
third = int(input("Enter number : "))

lst = []
lst.append(first)
lst.append(second)
lst.append(third)

for i in range(0 ,3):
	for j in range(0, 3):
		for k in range(0, 3):
			if i!=j and j!=k and k!=i:
				# print
				print(lst[i], lst[j], lst[k])

# ----------------

# GCD and LCM

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def main():
	a = int(input("Enter number : "))
	b = int(input("Enter number : "))

	lcm = (a * b) / gcd(a, b)
	print("LCM : ", lcm)
	print("GCD : ", gcd(a, b))

main()

# ----------------

# 2
# sum of natural numbers till n using recursion

def sum_recursion(n):
	# base case
	if n == 0 or n == 1:
		return 1
	return sum_recursion(n - 1) + n

print(sum_recursion(5))

# ----------------

# dictionary with key as first character and value as second

string = input("Enter string : ") # "samit sumit"
lst = string.split()
dictionary = {}

# for each word in the list (samit)
for word in lst:
	# if s not in dictionary -> add.
	if word[0] not in dictionary.keys():
		# add
		dictionary[word[0]] = [] # key
		dictionary[word[0]].append(word) # value s is mapped to s (s : samit)
	else:
		# samit already there, new entry -> sumit, so just check if it is already present or not and add it next to samit (s : samit, sumit)
		if word not in dictionary[word[0]]:
			dictionary[word[0]].append(word) # mapped to s (s : samit, sumit)

# print
# d.items() -> used to return the list with all dictionary keys with values
for key, value in dictionary.items():
	print(key, " : ", value)

# ----------------

# 3 
# rotate list k times

def rotate(lst, k):
	# base case if k is neg
	if k < 0:
		return lst
	else:
		lst2 = lst # new dummy lst2
		for i in range(0, k):
	        # last number + remaining (do this for k times)
	        # 1 2 3 4, -> 4 + [1,2,3] = [4,1,2,3]
			lst2 = [lst2[-1]] + lst2[0 : -1]
		return lst2

size = int(input("Enter size of list : "))
lst = []
for i in range(0, size):
	elem = int(input("Enter element : "))
	lst.append(elem)

print("Entered list : ", lst)
k = int(input("Enter number of rotations : "))
print("Rotated list : ", rotate(lst, k))

# ----------------

# common letters in strings

string1 = input("Enter string : ")
string2 = input("Enter string : ")
ans = set(string1) & set(string2) # if you need list -> list(set(string1) & set(string2))
print("Common letters : ", ans) # or for i in ans: print(i) -> if list needed

# ----------------

# 4

# count number of characters in string and store in dictionary -> samit mohan -> samit : 5, mohan : 5

string = input("Enter string : ")
lst = string.split() # ['samit', 'mohan']
dictionary = {}
for word in lst:
	if word not in dictionary.keys():
		# add it
		dictionary[word] = len(word) # map the word (samit) to the length (5)

#print
for key, value in dictionary.items():
	print(key, " : ", value)

# ----------------

# print first 10 lines and last 10 line of a file

file = input("Enter file name : ")
with open(file) as f:
	string = f.read() # read the file in string manner
	lst = string.split("\n") # split into list based on new line character
	print("First 10 lines : ")
	for i in lst[:10]:
		print(i)
	print("Last 10 lines")
	for i in lst[-10:]:
		print(i)

f.close()

# ----------------

# 5

# computer number of characters, words, lines in a file + most freq word read.

file = input("Enter file name : ")
dictionary = {}
with open(file) as f:
	line_count = 0
	word_count = 0
	character_count = 0
	for lines in f:
		line_count += 1
		character_count += len(lines)
		# for word -> split lines into words
		lst = lines.split()
		for word in lst: # word not in dictionary so add as value
			# if word not in dictionary -> then set count = 1
			if word not in dictionary.keys():
				dictionary[word] = 1
			else:
				# word already in dictionary -> count++
				dictionary[word] += 1

		word_count += len(lst)

	print("Lines : ", line_count)
	print("Words : ", word_count)
	print("Characters : ", character_count)
	# dictionary
	print(dictionary)

	# max value
	mx = max(dictionary.items(), key = lambda x : x[1]) # in dictionary items, word with most index values (lambda x : x[1]) is the max
	lst_keys = list()
	# iterate over all items in dictionary to find keys with max value
	for key, value in dictionary.items():
		if value = mx[1]:
			lst_keys.append(key)

	print("Word most freq used : ", lst_keys)
f.close()

# ----------------

# import from * -> create calc consists of 4 functions (sum, div, muk, subtr)
# create another module called user, import calc module and illustrate use

# Create new file in the same directory -> calc.py and write this
def add(a, b):
	res = a + b
	return res

def sub(a, b):
	res = a - b 
	return res

def mul(a, b):
	res = a * b 
	return res

def mul(a, b):
	res = a / b 
	return res


# Another file -> user.py
import calc
from calc import add, sub
print(calc.add(5, 2))
print(calc,sub(5, 2))

# another way
import calc as c 
print(c.mul(5, 2))

# ----------------

# 6
# Email Messaging

# library -> smtplib
import smtplib
gmail_add = input("Enter gmail address : ")
gmail_pass = input("Enter gmail password : ")
msg = input("Enter message : ")
mail_to = input("Enter reciever's mail address : ")

# start mail server
mailServer = smtplib.SMTP("smtp.gmail.com", 587) # remember

mailServer.ehlo() # ehlo
mailServer.starrtls() # start tls
mailServer.login(gmail_add, gmail_pass)
mailServer.sendmail(gmail_add, mail_to, msg)
print("Sent")
mailServer.quit()

# ----------------

# 7

# append delete display using classes and objects

class calculation:
	# default + functions
	def __init__(self):
		self.number = [] #  empty list

	def add(self, a):
		return self.number.append(a)
	def remove(self, b):
		return self.number.remove(b)
	def display(self):
		return self.number

# create new object
obj = calculation()
choice = 1
while choice != 0:
	print("0. Exit")
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	choice = int(input("Enter choice : "))
	if choice == 1:
		number = int(input("Enter number to add : "))
		obj.add(number)
		print("List : ", obj.display())
	elif choice == 2:
		obj.remove(number)
		print("List : ", obj.display())
	elif choice == 3:
		print("List : ", obj.display())

	elif choice == 0:
		print("Exiting")
	else:
		print("Invalid choice!")

# ----------------

# 8 

#complex number calc (you use magic methods)

class complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __add__(self, other):
		return self.a + other.a, self.b + other.b

	def __sub__(self, other):
		return self.a - other.a, self.b - other.b

	def __mul__(self, other):
		return self.a * other.a, self.b * other.b

	# string
	def __str__(self):
		return self.a, self.b

	# display
	def display(self):
		if self[1] > 0: # if i is not 0.
			print(self[0], " + ", self[1], "j", sep = " ") # number + j
		else: # if i = 0, only j remains.
			print(self[0], self[1], "j", sep = " ") # numbers j

obj1 = complex(1, 2)
obj2 = complex(1, 2)
add = obj1 + obj2
sub = obj1 - obj2
mul = obj1 * obj2

print("Addition : ", add)
complex.display(add)
print("Subtraction : ", sub)
complex.display(sub)
print("Multiplication : ", mul)
complex.display(mul)

# ----------------

# 9 
# Demonstrate the concept of Method Resolution order in multiple inheritance in Python Program.

import math

class Rectangle:
	def calc_area(length):
		breadth = length
		area = length * breadth
		print("Area of rectangle : ", area)

class Square:
	def calc_area(side):
		area = side * side
		print("Area of square : ", area)


class Circle:
	def calc_area(radius):
		area = 2 * math.pi * r ** 2 # 2 pi r^2
		print("Area of circle : ", area)

# multiple inheritance (passing all three in Shape)
class Shape(Square, Circle, Rectangle):
	pass

Shape.calc_area(10) # should print area of square = 100

# ----------------

# 10

# Exception handling

# Create a Python Program to take care of Number Format Exception if user enters values other than integer for calculating average marks of 2 students. 
# The name of the students and marks in 3 subjects are taken from the user while executing the program.
# In the same Program create your own Exception classes to take care of Negative values and values out of range (i.e. other than in the range of 0-100) 
# Include finally to output the statement : Program terminated.

class myException(Exception):
    # default constructor
    def __init__(self, arg):
        self.msg = arg

def marks(student_name):
    student_marks = list(map(float, input("Enter marks seperated by space : " ).split()))
    for mark in student_marks:
        if mark < 0 or mark > 100: # raise custom exception
            raise myException("Value neg or out of range!")

    sum_marks = sum(student_marks)
    print(student_name, "got", student_marks, "marks")
    return sum_marks

# try and except -> main program
try:
    s1 = input("Enter student 1 name : ")
    s1_marks = marks(s1)
    s2 = input("Enter student 2 name : ")
    s2_marks = marks(s2)
    print("Average : ", (s2_marks - s1_marks) / 6) # 6 -> 3 numbers each
except myException as e: # e => error message
    # custom exception
    print(e.msg)
except Exception as e:
    # default exception
    print("Number format error!", e)
finally:
    print("Program terminated!")

# ----------------

# 12

# Design & Implement the program in python to handle the events in an Application.
# python -m pip install pyautogui (windows) 
# pip install pyautogui (linux)

import pyautogui, time
time.sleep(5) # 5 second

# rotate mouse 10 times

def rotate():
	for i in range(10):
		pyautogui.moveTo(100, 100, duration = 0.25)
		pyautogui.moveTo(200, 100, duration = 0.25)
		pyautogui.moveTo(200, 200, duration = 0.25)
		pyautogui.moveTo(100, 200, duration = 0.25)

# drag in paint
# when going left or right -> distance = distance - 5
def drag():
	time.sleep(5)
	pyautogui.click() # click to put drawing program
	distance = 200
	while distance > 0: # runs 200 times
		pyautogui.drawRel(distance, 0, duration = 0.2) # start from distance, towards right
		distance = distance - 5 # sleep time
		pyautogui.drawRel(0, distance, duration = 0.2) # start 0 and go down
		pyautogui.drawRel(-distance, 0, duration = 0.2) # left (opp of right)
		distance = distance - 5 # sleep time
		pyautogui.drawRel(0, -distance, duration 0.2) # up (opp of down)


# screenshot
def take_screenshot():
	image = pyautogui.screenshot()
	image.save("screenshot.png")

# auto typing
def typing():
	time.sleep(5)
	pyautogui.typewrite("hello world", 1) # typewrite -> 2 parameters, (msg, 1)

# main
choice = 1
while choice != 0:
	print("0. Exit")
	print("1. Rotate Mouse")
	print("2. Drag in Paint")
	print("3. Take Screenshot")
	print("4. Autotyping")
	choice = int(input("Enter choice : "))
	if choice == 1:
		rotate()
	elif choice == 2:
		drag()
	elif choice == 3:
		take_screenshot()
	elif choice == 4:
		typing()
	elif choice == 5:
		print("Exiting")
	else:
		print("Invalid choice!")

# run program
print()

# output : The mouse and keyboard events are automated with the program and observed.

# ----------------

# 11 

# Design and Implement the program in python to manipulate images
# python -m pip install pillow (On Windows Installation)
# pip install pillow (On Linux Installation)

from PIL import Image
cat_image = Image.open('kyle.png')
print(cat_image.size)
print("Filename = ", cat_image.filename, "File format : ", cat_image.format)

img = Image.new('RGBA', (100, 200), 'purple')
img.save('purple_image.png')
img2 = Image.new('RGBA', (20, 20)) # transparent
img2.save('transparent_image.png')

cropped_img = cat_image.crop((335, 345, 565, 560))
cropped_img.save('cropped.png')

cat_image_copy = cat_image.copy()
face_image = cat_image_copy((335, 345, 565, 560))
cat_image_copy.paste(face_image, (0, 0))
cat_image_copy.paste(face_image, (400, 500))
cat_image_copy.save('pasted.png')

cat_image_width, cat_image_height =cat_image.size
face_image_width, face_image_height = face_image.size

cat_image_copy2 = cat_image_copy()
for left in range(0, cat_image_height, face_image_height):
	for top in range(0, cat_image_height, face_image_height)
		print(left, top)
		cat_image_copy2.paste(face_image, (left, top))

cat_image_copy2.save("tiled.png")

width, height = cat_image.size

quarter_sized_image = cat_image.resize(int(width/2), int(height/2))
quarter_sized_image.save('quartersized.png')
svelte_image = cat_image.resize((width, height + 300))
svelte_image.save('svelte.png')

cat_image.rotate(90).save('rotated90.png')
cat_image.rotate(180).save('rotated180.png')
cat_image.rotate(270).save('rotated270.png')

cat_image.rotate(6).save('rotated6.png')
cat_image.rotate(5, expland = True).save('rotated6_explanded.png')

cat_image.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal.png')
cat_image.transpose(Image.FLIP_TOP_BOTTOM).save('vertical.png')
