#father mother skills


class father:
    def skills(self):
        print("coding, fishing")
        
        
class mother:
    def skills(self):
        print("cooking, cleaning")
                
                
'''class child(father, mother):
    pass
    '''
class child(father, mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)

c = child()
c.skills()               