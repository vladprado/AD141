from person import Person
from family import Family

p1 = Person("Vladimir", 44, "M")
print(p1)

mother = Person("Mom", 45, "F")
father = Person("Dad", 45, "M")
kid1 = Person("Johnnie", 2, "M")
kid2 = Person("Janie", 3, "F")
my_family = Family(mother, father, kid1, kid2)
the_smiths = Family(father, mother, kid2)
print(my_family)
print(the_smiths)

print(my_family < the_smiths)
print(my_family > the_smiths)
print(my_family == the_smiths)
