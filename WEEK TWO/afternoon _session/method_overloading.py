#we deal with methods
#methods carry parameters
#methods are called
#method overloading, we have two or more methods having the same names but different kinds of parameters
#python does not support method overloading by default


def sum(w,r):
    s=w + r
    print(s)
    
    
    
def sum(w,r,x):
    s= w+ r + x
    print(s)
    
#sum(1,2,3)    #you will able to get a result for the latest defined  method  . thats how python works
sum(2,3,7)  



#product
def product(x,y):
    p=x*y
    print(p)
    
def product(x,y,z)  :
    p=x*y*z
    print(p)  
    
product(1,2,3)  

#if i had run the product(4,5). i would get an error because python only runs the latest method by default in method overriding.


#how to solve that , such that we can be able to call the first method without getting errors  
#pip - preffered installer packages(helps install packages)
#it's a standard package manager
#C:\Users\Bridget\AppData\Local\Microsoft\WindowsApps\python.exe. where my python is.

#we need to also download multipledispatch
#use pip install multipledispatch, for verification to know if you fully have it, you use the command , pip show multipledispatch
'''from multipledispatch import dispatch

@dispatch(int,int,int)

def sum (a,b,c):
    result=a+b+c
    print(result)
    
@dispatch(float,float,float)
def sum(w,r,t):
   result= w + r + t 
   print(result)   
   
   
sum(2,3,4)
sum(3.1,2.2,3.5)  
''' 