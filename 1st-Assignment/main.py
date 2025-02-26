#variable & Data type
name = "Humema Israr"
age = 20
height = 5.3
my_list =[1,2,3,4]
my_set = {1,2,3,4}
i_am = True
tuple = (1,2,3,4)
nonetype = None
dict = {"name" : "Humema" }


#Strings (str): Text, jaise "Hello", "Python", "123".Strings ko single (' ') ya double (" ") quotes mein likha ja sakta hai.
print(type(name))
print("my name is" ,name)
#Integers (int): Poore numbers, jaise 5, -10, 100.
print(type(age))
print("My age is" , age)
#Floats (float): Decimal numbers, jaise 3.14, 0.5, -2.7.
print(type(height)) 
print("My height is" ,height)
#Lists: Multiple values ko store karne ke liye, jaise [1, 2, 3, 4].
print(type(my_list))
print(my_list)
#Sets: Unique values ko store karne ke liye, jaise {1, 2, 3}.
print(type(my_set))
print(my_set)
#Booleans (bool): True ya False.
print(type(i_am))
print(i_am)
#Tuples: Lists ki tarah, lekin immutable (change nahi ho sakte), jaise (1, 2, 3).
print(type(tuple))
print(tuple)
#None is nothing
print(type(nonetype))
print(nonetype)
#Dictionaries: Key-value pairs ko store karne ke liye, jaise {"name": "Ali", "age": 25}.
print(type(dict))
print(dict)


# if-else keyword example  
age = 18  
if age >= 18:  
    print("You are an adult.")  
else:  
    print("You are a minor.")  

# for loop keyword example  
for i in range(5):  
    print(i)  

# def keyword example  
def greet(name):  
    print(f"Hello, {name}!")  

greet("Ali")  


# Python mein keywords wo special reserved words hote hain jo language ke rules aur structure ko define karte hain.
#  Inhe variable names ya identifiers ke taur par istemaal nahi kiya ja sakta. Python mein total 35 keywords hote hain.
#  Ye hain wo:

# Python Keywords List
# and: Logical AND operator.

# as: Alias banane ke liye (e.g., import math as m).

# assert: Debugging ke liye condition check karta hai.

# break: Loop se bahar nikalne ke liye.

# class: Class banane ke liye.

# continue: Loop ke agle iteration par jane ke liye.

# def: Function define karne ke liye.

# del: Object ko delete karne ke liye.

# elif: if ke saath multiple conditions ke liye.

# else: if condition false ho to execute hota hai.

# except: Exceptions handle karne ke liye.

# False: Boolean false value.

# **`finally``: Try-except block ke baad hamesha execute hota hai.

# for: Loop chalane ke liye.

# from: Module se specific functions import karne ke liye.

# global: Global variable declare karne ke liye.

# if: Condition check karne ke liye.

# import: Modules ko include karne ke liye.

# in: Check karta hai ke koi value list, tuple, dictionary, etc. mein hai ya nahi.

# is: Check karta hai ke do objects same hain ya nahi.

# lambda: Anonymous function banane ke liye.

# None: Null value ya kuch nahi hone ka representation.

# nonlocal: Nested functions mein outer function ke variable ko modify karne ke liye.

# not: Logical NOT operator.

# or: Logical OR operator.

# pass: Empty block ko define karne ke liye (placeholder).

# raise: Exception manually throw karne ke liye.

# return: Function se value return karne ke liye.

# True: Boolean true value.

# try: Exceptions handle karne ke liye block define karta hai.

# while: Condition true ho to loop chalane ke liye.

# with: Context managers ke saath use hota hai (e.g., file handling).

# yield: Generator function se value return karne ke liye.