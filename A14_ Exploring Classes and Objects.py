#define the class vehicle

class vehicle:
    
    def __init__(self, model, make, cost, year):
        self.model = model
        self.make = make
        self.cost = cost
        self.year = year

    def getDetails(self):
        print("Model : " + self.model)
        print("Make : " + self.make)
        print("cost : " + self.cost)
        print("Year : " + self.year)
        

# Creating an instance
us_vehicle = vehicle("Rav 4", "toyota", "35000", "2008")
vehicle.getDetails(us_vehicle)


