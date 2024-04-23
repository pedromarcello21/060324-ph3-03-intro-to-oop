class Human:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    def __repr__(self):
        return f"Human(first_name={self.first_name}, last_name={self.last_name})"
    
    def say_full_name(self):
        return self.first_name + " " + self.last_name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        raise ValueError('Quit lying about your age!')

    def happy_birthday(self):
        self._age = self.age + 1