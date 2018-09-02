## l1=[]
# l2=[]
# l=[]

# def fib(n):
#     a,b = 0, 1
#     while b<n:
#         l1.append(b)
#         a,b = b, a+b

# def prime(n):
#     for i in range(1, n):
#         for j in range(2,i-1):
#             if i%j==0 : break
#         else:
#             l2.append(i)
#             # print(i, end=" ") 
            
# n=int(input("no:"))

# # for i in range()
# # if(n%2==0):
# #     print(l1)
# # else:
# #     print(l2)
# t,k=0,0
# for i in range(0,n,2):
#     try:
        
#         l[i]=l1[k]
#         k+=1
#         l[i+1]=l2[t]
#         t+=1
#     except:
#         break
# print(l)



# factorial
# def fact(n):
#     f=1
#     for i in range(1, n+1):
#         f=f*i
#     return f


# area of triangle
# def area(x,y):
#     area=0.5*x*y
#     print(area)
# x = int(input("l"))
# y = int(input("h"))
# area(x,y)

# leap yr
# def leap(n):
#     if(n%4==0 and n%100!=0):
#         print("leap yr")
#     elif(n%400==0):
#         print("leap yr")
#     else:
#         print("not a leap yr")
        
# x = int(input("yr"))
# leap(x)



# gcd
# def gcd(a,b):
#     if a>b:
#         small=b
#     else:
#         small=a
#     for i in range(1, small+1):
#         if((a%i==0) and b%i==0):
#             gcd=i
#     return gcd
# a=int(input("a:"))
# b=int(input("b:"))
# print(gcd(a,b))  


# check prime no if prime output will be square of no if not output is 0.00
# def prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             print (n, " is not prime")
#             print("0.00")
#             break
#     else:
#         print(n, " is prime")
#         print(float(n*n))
        
# n=int(input("no:"))
# prime(n)




# to check strong no
# def factorial(n):
#     fact = 1
#     for i in range(2, n + 1):
#         fact = fact * i
#     return fact
 
# def check(x): 
#         tmp = x
#         sum = 0
#         while tmp != 0:
#             rem = tmp % 10
#             sum = sum + factorial(rem)
#             tmp //= 10
#         if sum == x:
#             print(x, "is strong no")
#             break
#         else:
#             print("not a strong no")
#             break
        
# x=int(input("no:"))
# check(x)

# to convert decimal to bin,oct,hexadecimal
# dec = 344

# print("The decimal value of",dec,"is:")
# print(bin(dec),"in binary.")
# print(oct(dec),"in octal.")
# print(hex(dec),"in hexadecimal.")\

# def convert(n):
#     print(bin(n))
    
# n=int(input("no:"))
# convert(n)


# sum of prime no of given range
# def sumprimes(m,n):
#     sum=0
#     for i in range (m+1,n+1):
#         li=[]
#         for j in range (1,i+1):
#             if i%j==0:
#                 li=li+[j]
#         if li==[1,i]:
#             sum=sum+i
#     return(sum)
    
# m=int(input("m:"))
# n=int(input("n:"))
# print(sumprimes(m, n))



# to check perfect square
# import math

# n = int(input())

# i = int(math.sqrt(n)) #sqrt function returns float so typecasting to int

# if(n == i*i):
#   print("perfect Square")
# else:
#   print("Not Perfect Square")




# # to check palindrome
# my_str = 'adhadhja'
# # make it suitable for caseless comparison
# my_str = my_str.casefold()
# # reverse the string
# rev_str = reversed(my_str)
# # check if the string is equal to its reverse
# if list(my_str) == list(rev_str):
#   print("It is palindrome")
# else:
#   print("It is not palindrome")
   
   
   
# def cube(n):
#     cube=n*n*n
#     return n
    
 
# def check(x): 
#         tmp = x
#         sum = 0
#         while tmp != 0:
#             rem = tmp % 10
#             sum = sum + cube(rem)
#             tmp //= 10
#         # print(sum)
#         if sum == x:
#             print(x, "is arm no")
#         else:
#             print("not a arm no")
        
# x=int(input("no:"))
# check(x)


# def capitalizeVowels(word):
#     for i in word:
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             a = i.upper()
#             word=word.replace(i, a)
#     print(word)
#     # return word

# n = input("word:")
# capitalizeVowels(n)


def check(x): 
    order = len(str(x))
    tmp = x
    sum = 0
    while tmp != 0:
        rem = tmp % 10
        sum = sum + rem**order
        tmp //= 10
    # print(sum)
    if sum == x:
        print(x, "is arm no")
    else:
        print("not a arm no")
        
x=int(input("no:"))
check(x)


# num = 1634
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#   digit = temp % 10
#   sum += digit ** order
#   temp //= 10
# if num == sum:
#   print(num,"is an Armstrong number")
# else:
#   print(num,"is not an Armstrong number")



# to find hypotenuse of triangle
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )
