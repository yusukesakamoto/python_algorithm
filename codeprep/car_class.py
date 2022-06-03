class Car:
    fuel = 100
    fuel_consumption = 10
    def __init__(self,fuel,fuel_consumption):
      self.fuel = fuel
      self.fuel_consumption=fuel_consumption
      
    def reachable(self,distance):
      return True if self.fuel*self.fuel_consumption > distance else False