class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=40
    
    def starting(self):
        print(f"The {self.year} {self.make} {self.model} is starting!")

    def update_odometer(self,new_reading):
        if new_reading<self.odometer:
            print("Odometer reading cannot decrease!")
        else:
            self.odometer=new_reading

    def inc_odometer(self, mileage):
        self.odometer+=mileage

class Battery:
    def __init__(self, battery=40):
        self.battery=battery #to edit DEFAULT value of 40

    def battery_amount(self):
        print(f"The vehicle has currently {self.battery}% of battery power.")
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.odometer=40
        self.battery=Battery() #bracket!! NO VALUE = default value used!

my_car = ElectricCar("Mercedes", "C class", 2024)
my_car.battery.battery_amount() #bracket!! function call!!

her_car = Car("Bentley", "Pro", 2024)
her_car.inc_odometer(69)
her_car.starting()
print(f"My girlfriend's car has {her_car.odometer}km worth of mileage.")
#Line 38 -- can use within CLASS/FXN a print statement!


    
