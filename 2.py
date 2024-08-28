'''
# printing the prize problem 
a = 53
b = 8
print('the number of prizes each get',(a//b))
print('the remaining number of prizes ',(a%b))
'''

'''
# displaying the info af an individual
name = input("enter the name")
gender = input("enter the gender")
age = int(input("enter the age"))
print('name ',name, '\n','age',age,'\n',"gender",gender)
print(type(age))
'''


'''
 # printing the square of a range
print('square of each number from 1 - 10')
for i in range(1,11):
  print(i**2)

l = [t*t for t in range(1,11)]
print(l)
'''


'''
# palindrome reverse etc
a = int(input("enter a number"))
n=a
b=0
while a > 0:
    b = b*10 + a%10 
    a = a//10
    
print(b)
if n==b:
  print("pal")
else:
  print(" not pal")

  '''


'''
 # pattern program
for i in range(1,6):
   for j in range(1,6):
    print(i*j,end=' ')
    
   print("")     
'''


'''
# prime not prime
a = int(input("enter the number: "))
b = int(0)
for i in range(2,a):
  if a%i == 0:
      print("np")
      break
  else:
     b = b+1
if b >0:
   print("p")
'''
























    
 
