#prime or not
num = 15
flag = 0
for i in range(2,num+1):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

#odd number using while loop
i=1
m=20
while i<=m:
   if i%2 !=0:
     print(i)
   i=i+1

#prime number in series 
def prime(n): 
    for i in range(2,n//2+1): 
        if(n%i==0): 
            return(0) 
    return(1) 
 
a = int(input("Enter a:")) 
b = int(input("Enter b:")) 
result = [] 
for i in range(a,b+1): 
    if(prime(i)): 
        result.append(i) 
print(result)

#write a program to print fibonacci series in python
import math

def fibonacciSeries(phi, n):
    for i in range(0, n + 1):
        result = round(pow(phi, i) / math.sqrt(5))
        print(result, end=" ")


num1 = 10
phi = (1 + math.sqrt(5)) / 2
fibonacciSeries(phi, num1)