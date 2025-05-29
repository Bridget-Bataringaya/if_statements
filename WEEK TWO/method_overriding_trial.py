class Animal:
  def makesound(self):
      print("The animal makes sound")
      
      
      
class cat(Animal):
    def makesound(self):
        print("the cat says meow")    
        
class dog(Animal):
    def makesound(self):
        print("the dog says roof roof")  
        
   #here your creating objects     
a = dog()
b = cat() 
c = Animal() 
 #then call the methods
a.makesound() 
b.makesound()
c.makesound()            