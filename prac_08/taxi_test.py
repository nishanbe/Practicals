"""Test Taxi"""
from prac_08.taxi import Taxi

"""
Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
Drive the taxi 40km
Print the taxi's details and the current fare
Restart the meter (start a new fare) and then drive the car 100km
Print the details and the current fare
"""

taxi1 = Taxi("Prius 1", 100, 1.23)
taxi1.drive(40)
print(taxi1)
