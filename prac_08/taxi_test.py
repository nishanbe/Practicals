"""Test Taxi"""
from prac_08.taxi import Taxi

"""
Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
Drive the taxi 40km
Print the taxi's details and the current fare
Restart the meter (start a new fare) and then drive the car 100km
Print the details and the current fare
"""

name = "Prius 1"
fuel = 100
distance = 40

taxi1 = Taxi(name, fuel)
taxi1.drive(distance)
print(taxi1)

taxi1.start_fare() # Restart the meter
distance2 = 100

taxi1.drive(distance2)
print(taxi1)