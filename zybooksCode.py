class Person:
   def __init__(self):
      self.first_name = ""
      self.last_name = ""

   def get_full_name(self):
      return self.last_name + " " + self.first_name

a_first_name = "Ann"
another_first_name = "Ron"
a_last_name = "Stark"
another_last_name = "Rogers"

person1 = Person()
person2 = Person()

person1.first_name = a_first_name
person1.last_name = a_last_name
person2.first_name = another_first_name
person2.last_name = another_last_name

print(f"You are {person1.get_full_name()}")
print(f"I am {person2.get_full_name()}")