"""Silver Service Taxi Test"""
from prac_08.silver_service_taxi import SilverServiceTaxi

# Assign a name, set a fuel level and fanciness
car = SilverServiceTaxi("Hummer", 0, 2)
car.add_fuel(200)

# Drive 18KM
car.drive(18)
fare = car.get_fare()

# Display the result
print("{}\nA total fare of ${:,.2f}".format(car, fare))

















