#key principles in OOP
#inheritance
#polymorphism
#method overriding and method overloading
#abstraction
#encapsulation



#inheritance
#example one. 
#super class / parent class/ based class

class Animal:
    def speak(self):
              print("Animal makes sound")
              
              
              
#subclass/ child class / derived class
class cat(Animal):
    def sound(self):
        print("cat makes sound moew")   
        
#create object of cat
cat1 =cat()

#calling the inherited method 
cat1.speak() 

#calling the subclass method
cat1.sound()                  

#roy qtns 
#use special method called _init_

class person:
    def _init_(self,fname,lname):
        self.firstname= fname
        self.lastname= lname
        
    def printname(self):  
        print()  
        
        
        
        
        
        #polymorphism
        # what is polymorphism
        
        #Example Three: Polymorphism with inheritance
        #Supeerclass
class Bird:
        def fly(self):
                print('Birds flies in the sky')
        
        #derived class
class Eagle(Bird):
            def fly(self):
                print('Eagle flies at high altitude')
class sparrow(Bird):
    def fly(self):
        print("sparrow flies at a low altitude")   
        
        #how we use polymorphism
def flight_test(bird):
    bird.fly() # run repective class method based on an object
        
#create objects
eagle1= Eagle()
sparrow1= sparrow()
       
       
flight_test(eagle1)
flight_test(sparrow1)                
    