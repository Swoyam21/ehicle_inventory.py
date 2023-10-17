# Step 1: Creating a class named Vehicle with the following attributes make, model, year, vin and price

class Vehicle:
    def __init__(self, make, model, year, vin, price):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price

# Displaying all the details of the Vehicle.  
    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"VIN: {self.vin}")
        print(f"Price: {self.price}")


# Step 2: Creating SubClasses for Car, Truck and Motorcycle

class Car(Vehicle):

# Adding some addtional attributes for number of doors and fuel type.  
    def __init__(self, make, model, year, vin, price, doors, fuel_type):
        super().__init__(make, model, year, vin, price)
        self.doors = doors
        self.fuel_type = fuel_type

    def display_details(self):
        super().display_details()
        print(f"Doors: {self.doors}")
        print(f"Fuel Type: {self.fuel_type}")


class Truck(Vehicle):

# Adding some additional attributes for cargo capacity and towing capacity.  
    def __init__(self, make, model, year, vin, price, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, vin, price)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def display_details(self):
        super().display_details()
        print(f"Cargo Capacity: {self.cargo_capacity}")
        print(f"Towing Capacity: {self.towing_capacity}")


class Motorcycle(Vehicle):

# Adding some additional attribute for style of Motorcycle.  
    def __init__(self, make, model, year, vin, price, style):
        super().__init__(make, model, year, vin, price)
        self.style = style

    def display_details(self):
        super().display_details()
        print(f"Style: {self.style}")

# Step 3: Implementing a method in each subclass that calculates the total cost of the vehicle, including any additional fees, taxes, or discounts.

class Car(Vehicle):
    def __init__(self, make, model, year, vin, price, doors, fuel_type):
        super().__init__(make, model, year, vin, price)
        self.doors = doors
        self.fuel_type = fuel_type

    def calculate_total_cost(self):
        return self.price * 1.1  # adding 10% tax for cars

# Step 4: Creating a VehicleInventory class that represents the dealership’s inventory of vehicles.

class VehicleInventory:
    def __init__(self):
        self.inventory = []

    def add_vehicle(self, vehicle):
        self.inventory.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.inventory.remove(vehicle)

    def display_inventory(self):
        for vehicle in self.inventory:
            vehicle.display_details()
            print()
          
# Step 5: Implementing polymorphism by using a common method name,

class Vehicle:
    def __init__(self, make, model, year, vin, price):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price

    def display_details(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("VIN:", self.vin)
        print("Price:", self.price)

class Car(Vehicle):
    def __init__(self, make, model, year, vin, price, doors, fuel_type):
        super().__init__(make, model, year, vin, price)
        self.doors = doors
        self.fuel_type = fuel_type

    def display_details(self):
        super().display_details()
        print("Doors:", self.doors)
        print("Fuel Type:", self.fuel_type)

class Truck(Vehicle):
    def __init__(self, make, model, year, vin, price, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, vin, price)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def display_details(self):
        super().display_details()
        print("Cargo Capacity:", self.cargo_capacity)
        print("Towing Capacity:", self.towing_capacity)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, vin, price, engine_type):
        super().__init__(make, model, year, vin, price)
        self.engine_type = engine_type

    def display_details(self):
        super().display_details()
        print("Engine Type:", self.engine_type)


# Showing the implemention

my_car = Car("Toyota", "Camry", 2022, "ABC123", 25000, 4, "Gas")
my_car.display_details() # Prints out all details of the car

my_truck = Truck("Ford", "F-150", 2022, "DEF456", 35000, 5000, 10000)
my_truck.display_details() # Prints out all details of the truck

my_motorcycle = Motorcycle("Harley Davidson", "Road King", 2022, "GHI789", 20000, "V-Twin")
my_motorcycle.display_details() # Prints out all details of the motorcycle




# For Extra Credit # 

class Vehicle:
    def __init__(self, make, model, year, vin, price):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price

    def display_details(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("VIN:", self.vin)
        print("Price:", self.price)

class Car(Vehicle):
    def __init__(self, make, model, year, vin, price, doors, fuel_type, mileage=0):
        super().__init__(make, model, year, vin, price)
        self.doors = doors
        self.fuel_type = fuel_type
        self.mileage = mileage

    def calculate_total_cost(self):
        return self.price - (self.mileage * 0.1)

    def display_details(self):
        super().display_details()
        print("Doors:", self.doors)
        print("Fuel Type:", self.fuel_type)
        print("Mileage:", self.mileage)

class Truck(Vehicle):
    def __init__(self, make, model, year, vin, price, cargo_capacity, towing_capacity, mileage=0):
        super().__init__(make, model, year, vin, price)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
        self.mileage = mileage

    def calculate_total_cost(self):
        return self.price - (self.mileage * 0.15)

    def display_details(self):
        super().display_details()
        print("Cargo Capacity:", self.cargo_capacity)
        print("Towing Capacity:", self.towing_capacity)
        print("Mileage:", self.mileage)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, vin, price, engine_type, mileage=0):
        super().__init__(make, model, year, vin, price)
        self.engine_type = engine_type
        self.mileage = mileage

    def calculate_total_cost(self):
        return self.price - (self.mileage * 0.05)

    def display_details(self):
        super().display_details()
        print("Engine Type:", self.engine_type)
        print("Mileage:", self.mileage)

# creating instances of used vehicles and calculate their total cost.

my_used_car = Car("Toyota", "Camry", 2020, "ABC123", 25000, 4, "Gas", 20000)
print("Total Cost:", my_used_car.calculate_total_cost()) # Prints the total cost of the used car.


