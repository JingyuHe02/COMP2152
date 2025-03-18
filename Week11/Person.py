class Person:
    def __init__(self, p_name, p_age, p_height):
        print("Constructing the person object")
        self.name = p_name
        self.age = p_age
        self.height = p_height
        self.public_prop = "I'm public"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def _del_(self):
        print("The garbage collector is automatically destroying the person object!")
        
person1 = Person("Mark", 20, 6)

print("The name of the person is: " + str(person1.name))
# print("Private: " + str(person1.__name)) #This will give an error
person1.name = "Alfred"
print("The name of the person is: " + str(person1.name))

print("Public: " + str(person1.public_prop))