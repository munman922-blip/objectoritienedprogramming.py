class Vehicle:
    def __init__(self,max_speed,mileage):
      self.max_speed=max_speed
      self.mileage=mileage
    def display(self):
        print("Max speed is",self.max_speed)
        print("Mileage is",self.mileage)
car=Vehicle(400,65)
truck=Vehicle(210,18)
car.display()
truck.display()