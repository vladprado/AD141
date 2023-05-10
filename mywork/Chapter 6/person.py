class Person:

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender
    
    def __str__(self) -> str:
       return self._name +", " + str(self._age) + " years old is " +  self._gender

    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, gender):
        self._gender = gender