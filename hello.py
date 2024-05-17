#block of rusable code that performs a specific task
#organising code in function we can reuse it as many times as we wanr
#Function accepts optional input inform of arg and return an output
#fuctions only run when called /invoked/execute
#To define a function  def keyword is used followed by name of funtion and ():
#body of a funtion is idented
#name is arg


#1 studen@student-ThinkPad-E14-Gen-4:~/pythonClass/functions$ python3
# Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>>  hello()
#   File "<stdin>", line 1
#     hello()
# IndentationError: unexpected indent
# >>> from hello import hello
# >>> hello()
# Hello Akirachix
# >>> hello
# <function hello at 0x7b76bf1960e0>
# >>> hello()
# Hello Akirachix
# >>> 
# [4]+  Stopped                 python3


# def hello():
#    print(f"Hello AkiraChix")
#    #hello()
   
# 2studen@student-ThinkPad-E14-Gen-4:~/pythonClass/functions$ python3
# Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from hello import hello
# >>> hello()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: hello() missing 1 required positional argument: 'name'
# >>> hello("Amanda")
# Hello Amanda
# >>> hello("Jane")
# Hello Jane
# >>> 



# def hello(name):
#    print(f"Hello {name}")
#    #hello()
   

# 3>>> from hello import year_of_birth
# >>> year_of_birth()
# >>> year_of_birth("Anne",23)
# Hello Anne you are in 2001
# >>> year_of_birth("Brenda",20)
# Hello Brenda you are in 2004
# >>> year_of_birth("Ken",50)
# Hello Ken you are in 1974
# >>> 



def year_of_birth(name,age):
  year = 2024 - age
  print(f"Hello {name} you were born in {year}")

# >>> from hello import year_of_birth
# >>> year_of_birth("Brenda",20)
# Hello Brenda you were born in 2004
#   year_of_birth(name="Brenda",age=15)
# Hello Brenda you were born in 2009
# >>> year_of_birth(age=15,name="Ann")
# Hello Ann you were born in 2009
#    year_of_birth(15,"Ann")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/studen/pythonClass/functions/hello.py", line 66, in year_of_birth
#     year = 2024 - age
# TypeError: unsupported operand type(s) for -: 'int' and 'str'



#    functioning naming rules ,syntax rule
#   1. function name cannot start with a number it starts with a letter.
#   2.  ''                  contain spaces.   
#   3.If your function has more than one name combine them with underscore no camelCase convetion

#    convectional rule
#   4.Function name in lowercase
#   5.function name should be descriptive of what function does english

def my_country(country= "Uganda"):
  print(f"Hello,am from Akirachix in {country}")


#   >>> from hello import my_country
# >>> my_country()
# Hello,am from Akirachix in Ugande
# >>> my_country()
# Hello,am from Akirachix in Ugande
# >>> my_country("Kenya")
# Hello,am from Akirachix in Kenya
# >>> my_country("Rwanda")
# Hello,am from Akirachix in Rwanda
# >>> 

# *args

def hello(name):
 print (f"Greet {name}")

 """from hello import hello
>>> hello("Hannah")
Greet Hannah
"""

def greet(*name):
 print (f"Greet {name}")

"""greet("Hannah","Waluse","John")
Greet ('Hannah', 'Waluse', 'John')
>>> 
"""



"""Function that accepts any number of keyword arguments
One parameter **   two stars to dic"""


def create_dic(**words):
  print(words)
  sentence = ""
  for word in words.values():
   sentence += word
   sentence += " "

  return sentence 
  # current one

""""Position that accepts any number of positional arguments and any number 
of keyword arg
* in the first parameter and ** in the second parameter"""


"""args, kwargs"""


def sum_of_greet(*args,**kwargs):
  total = 0
  for x in args:
    total += x
  f = kwargs['FirstName']  
  l = kwargs['LastName']
  greeting = f"Hello {f} {l} and {total}"
  # greeting = f"Hello {f} {l} and {total} " if it is not their it wont print at all



  return greeting


"""">>> from hello import sum_of_greet
>>> sum_of_greet(10,12,13,14,15,FirstName = 'Brenda',LastName = 'Khamali')
'Hello Brenda Khamali and 64'
>>> 
"""


"""Control Flow
object oriented programming  class,attributes,behavior
Backend system"""