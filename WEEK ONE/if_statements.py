#equal a == b
#not equal a != b
#greater than a > b
#less than a < b
#greater than or equal to a >= b
#less than or equal to a <= b



#if statements

age = 20
if age >= 18:
    print("you are an adult")
elif age >=13:
    print("you are a teenager") 
else:
    print("you are a child") 
    
    #EXERCISE 1
    #.QN Grade basic using if statements, elif statement and else statement
    
marks=56
if marks >= 75:
        print("GOOD PERFORMANCE")
elif marks >= 50:
        print("AVERAGE PERFORMANCE")
else:
        print("POOR PERFORMANCE") 
        
        #nested if
        #scenario:    movie ticket booking system
        #rules 
        '''
        -a person must be 18 years to watch and rate a movie
        -if they are 18 years or older , check if they have a valid ticket
        -only if they have a valid tickect, and are 18 years or older they can watch the movie
        ''' 
        
        
age= int(input("Enter your age:"))    
if age >= 18:
    print("you are an adult")
    has_tickect= input("Do you have a tickect (yes/no):")
    if has_tickect == "yes":
        print("you can watch and rate a movie")
    else:
        print("you can not watch a movie nor rate it")    
else:
    print("you are under age to watch a movie") 
    
    
    
    #       trial on nested ifs(grade evaluator)
'''marks= int(input("Enter your marks:") )
if marks >= 50 :
    print("grage E")   
    if marks >= 60:
        print("grage D")             
    if marks >= 70 :
        print("grade C")   
    if marks >= 80:
        print("grade B")  
    if marks >= 90:
        print("grage A") 
else:
    print("the student has failed and they need to aim higher")              
    
    '''
    
    #correct code
    
marks = int(input("Enter your marks: "))

if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    elif marks >= 60:
        print("Grade D")
    elif marks >= 50:
        print("Grade E")
    else:
        print("The student has failed and they need to aim higher.")
else:
    print("Invalid marks. Please enter a number between 0 and 100.")
    