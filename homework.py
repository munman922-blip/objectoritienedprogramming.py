class Pet:
    print("Hi I am a pet profile programming class")
pet_obj=Pet()
class Pet_Profile:
    catogory='pet'
    def __init__(self,name,animal_type,colour,age,favourite_food):
        self.name=name
        self.animal_type=animal_type
        self.colour=colour
        self.age=age
        self.favourite_food=favourite_food
marcus=Pet_Profile('Marcus','Dog','White and brown',7,'Dog bone')
john=Pet_Profile('John','Dog','Brown',8,'Dog bone')
jonathan=Pet_Profile('Jonathan','Dog','Gold and brown',9,'Dog bone')
print(marcus.name, "fur is", marcus.colour, "He is a", marcus.animal_type, marcus.name, "favourite food is", marcus.favourite_food)
print(john.name,"fur is", john.colour, "He is a", john.animal_type, john.name, "favourite food is", john.favourite_food)
print(jonathan.name, "fur is", jonathan.colour, "He is a", jonathan.animal_type, jonathan.name, "favourite food is", jonathan.favourite_food)

