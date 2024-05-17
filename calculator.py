def add(x,y):
 result = x + y
 return result
# add(3,4)

def subtruct(x,y):
   result1 = x-y
   return result1
# subtruct(5,6)

def multiply(x,y):
    result2 = x*y
    return result2
# multiply(8,7)

def division(x,y):
   result3 = x/y
   return result3
# division(9,10)

def modulus(x,y):
   result4 = x%y
   return result4

def power(x,y):
   result5 = x**y
   return result5


def sum(*numbers):
  sum = 0
  for number in numbers:
    sum += number
  return sum

"""from calculate import sum
>>> sum(1,2,3,4,4,5)
19
>>> 
"""

def multiply_num(*numbers):
  multiply = 1
  for number in numbers:
    multiply *= number
  return multiply  

""" from calculate import multiply_num
>>> multiply_num(1,2,3,4,4,5,5)
2400
>>> 
"""