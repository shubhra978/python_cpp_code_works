class bike_detail:
    #constructor
    def __init__(self,model,cc):
        self.bike_name = model
        self.range = cc
        
    def info(self):
        print(f"bike name {self.bike_name} and {self.range}")
        
    @staticmethod #definition of static method
    def addition(x,y):
        print(x+y)


my_bike=  bike_detail("cb350rs",350)
my_bike2 = bike_detail("trimupt4",350) 
my_bike.info()
my_bike2.info()
bike_detail.addition(3,2)
