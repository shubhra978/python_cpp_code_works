#class definition
class car_details: 
    #defining attributes or variables
    model= "cb-350"
    variant= "rs"                   
    year= 2026
    mileage= 45
    engine_type= "air_cooled"
    price= "2,26,000"
    
    #defining method or function
    
    #attributes within function will take user attributes defined outside class calling from object
    def bike_type(self,model,variant):
        print(f"i want to buy a {model} {variant} ")
        
    #no attributes except self will call the attributes defined within the class 
    def bike_type_defined(self):
        #using self in f print to add the attribites defined
        print(f"i want to buy a {self.model} {self.variant} ")
        
        


my_car = car_details() #use parenthesis while assigning a class to an object
print(my_car.model)

print(my_car.bike_type("triump","t4"))
print(my_car.bike_type_defined())
