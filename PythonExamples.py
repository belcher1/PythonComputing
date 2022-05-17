# Python for Everybody (/56)

# # 6 Intermediate Expressions
# width = 15
# height = 12.0
# print(height/3)

# # 7 Conditional Execution
# if 0 == x:
#     if y == 10:
#         print("Yes")

# # 8
# temp = "5 degrees"
# cel = 0
# fahr = float(temp)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)

# # 10 Build your own Functions
# def fred():
#     print("Zap")
# def jane():
#     print("ABC")
# jane()
# fred()
# jane()

# # 11 Loops and Iterations
# n = 0
# while True:
#     if n == 3:
#         break
#     print(n)
#     n = n + 1

# # 12 
# for i in [2,1,5]:
#     print(i)

# # 13 Iterations: Loop Idioms
# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break # Does not loop due to the break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# # 15 Strings in Python
# for n in "banana":
#     print(n)

# # 16
# word = "bananana"
# i = word.find("na")
# print(i) #prints 2, counts 0, 1, 2 ???

# # 17 New line
# \n

# # 19 Python Lists
# fruit = "banana"
# x = fruit[1]

# # 20 Working with Lists
# Add an item to the end of the list with append()

# # 21
# words = 'His e-mail is q-lar@freecodecamp.org'
# pieces = words.split()
# parts = pieces[3].split('-')
# n = parts[1]

# # 22
# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9

# # 23 Dictionaries: Common Applicatoins
# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))

# # 24
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

# # 25 The Tuples Collection
# d = dict()
# d['quincy'] = 1
# d['beau'] = 5
# d['kris'] = 9
# for (k,i) in d.items():
#     print(k, i)

# # 26 Comparing and Sorting Tuples
# lst = []
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# print(lst)
# # or
# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

# # 27 
# \s matches only white space

# # 28
# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)