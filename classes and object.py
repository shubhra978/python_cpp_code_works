#class definition
class car_details: 
    #defining attributes or variables
    model= "cb-350"
    variant= "rs"                   
    year= 2026
    mileage= 45
    engine_type= "air_cooled"
    price= "2,26,000"
    speed = "0-30"
    top_speed = "143"
    
    #defining method or function
    
    #attributes within function will take user attributes defined outside class calling from object
    def bike_type(self,model,variant):
        print(f"i want to buy a {model} {variant} ")
        
    #no attributes except self will call the attributes defined within the class 
    def bike_type_defined(self):
        #using self in f print to add the attribites defined
        print(f"i want to buy a {self.model} {self.variant} ")
        
class new_car(car_details):
  def bike_speed(self):
    print(f"default bike speed {self.speed}")
class car_cabability(new_car):
  def bike_cap(self):
    print(f"bike top speed is {self.top_speed}")

#use parenthesis while assigning a class to an object
my_car = car_details() 
my_new_car = new_car()
car_top = car_cabability()

print(my_car.model)

print(my_car.bike_type("triump","t4"))
print(my_car.bike_type_defined())

#inheritance of a class call with an object
my_new_car.bike_speed()

car_top.bike_cap()
