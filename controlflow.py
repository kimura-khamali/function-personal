def print_Numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)

print_Numbers(10)

# if checks if a comparison is true or false or the score of the if statement is excuted


def print_Even_Numbers(n):
    numbers1 = range(n)
    for number in numbers1:
        if number % 2== 0:
         print(number)

print_Even_Numbers(1000)

# Else statement is completly optional 
# we can combine the if statyement with an optional else
# else statemnet is excuted if preciding if statement returns false


def odd_or_even(n):
   numbers2 = range(n)
   for number in numbers2:
      if number %2 == 0:
         print(f"{number} is even")
      else:
          print(f"{number} is odd")  
 
odd_or_even(100)

# Allows as to do more than one comparison


def check_divisibility(n):
   numbers = range(n)
   for number in numbers:
      if number %2 == 0:
          print(f"{number} is even")
      elif number %3 == 0:
         print(f"{number} is divisible bt 3")
      elif number %4== 0:
         print(f"{number} is divisible by 4")
      elif number %5== 0:
         print(f"{number} is divisible by 5")
      else:
         print(number)

check_divisibility(100)

"""while statement 
while loop continues to iterate as long as the set is true"""


def count_down(n):
   while n>0:
      print(n)   #it continues to loop
      n-=1

count_down(10)     


"""while break keyword
break statement stops the while loop even if the set condition is true"""


def count_down1(n):
   while n>0:
      print(n)
      if n == 0:
         break
      
      n-=1

count_down1(5)   

"""while continue statement
Skips the reminder of the current iteration of the while loop and jumps to the next iteration"""

def divisible_by_seven(n):
   x = 1
   while x<=n:
      n-=1
      if x%7 != 0:
         continue
      print(x)

divisible_by_seven(20)  

"""create function called fizzbuzz the function accepts a number n and generates a range of numbers from
0 to n .
for numbers divisible by 3 print fizz
for numbers divisible by 5 print buzz
for other number print fizzbuzz"""

def giveFizzorbuzz():
   for n in range(1,101):

     if n % 3 ==0:
      print(f"Fizz") 
     elif n% 5 ==0:
      print(f"Buzz")
     else:
       print(f"FizzBuzz")

giveFizzorbuzz()        
          



"""create a while ,if  with continue function to print all the even numbers from 0 to 50"""

def give_Even(n):
    x= 0
   
    while x<=n: 
      x+=1
      if x % 3 == 0:# even   x %2 == 0 odd
        continue
      else:
       print(x)
 

give_Even(50)


