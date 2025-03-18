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
        