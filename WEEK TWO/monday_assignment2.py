'''Concept: Instructors and Admins are Users. A super-admin can 
# be both. Method overriding is used for access, method overloading 
# is simulated with parameters, and MRO determines which class is prioritized.'''

# Base class
class User:
    def access(self, level=None):  # <-- Overloading via optional argument
        print("Basic user access.")

# Derived class
class Instructor(User):
    def access(self, level="instructor"):  # <-- Method Overriding from User
        if level == "instructor":
            print("Instructor access to course materials.")
        else:
            print("Instructor performing other tasks.")

# Another derived class
class Admin(User):
    def access(self, level="admin"):  # <-- Method Overriding from User
        if level == "admin":
            print("Admin access to system settings.")
        else:
            print("Admin performing other admin tasks.")

# Multiple inheritance
class SuperAdmin(Instructor, Admin):
    def access(self, level="superadmin"):  # <-- Method Overriding from Instructor/Admin
        if level == "instructor":
            super(Instructor, self).access(level)  # <-- MRO: Calls Admin
        elif level == "admin":
            super().access(level)                  # <-- MRO: Calls Instructor
        else:
            print("SuperAdmin has all-access privileges.")

# MRO shows the class resolution order
print(SuperAdmin.__mro__)  # <-- MRO in action

# Create object
sa = SuperAdmin()
sa.access("admin")        # <-- Overloading (input), MRO resolves to Instructor
sa.access("instructor")   # <-- Overloading (input), MRO resolves to Admin
sa.access("superadmin")   # <-- Overriding in SuperAdmin
