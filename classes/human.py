class Human:

    def __init__(self, first_name, last_name):
        print("I\'m making a person")
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    def __repr__(self):
        return f"This is {self.first_name} {self.last_name}, age: {self._age}"
    
    def say_full_name(self):
        return f"My name is {self.first_name} {self.last_name}"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if hasattr(self, 'age'):
            raise TypeError("Quit lying about your age")
        elif type(value)== int:
            self._age = value
        else:
            raise TypeError("Age must be an integer")
    
    def happy_birthday(self):
        self._age +=1


    pass