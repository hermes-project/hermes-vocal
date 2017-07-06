# Command-line Interface

import logging
from core import core
logging.basicConfig(level=logging.DEBUG)

print("######################")
print("#    Hermes-vocal    #")
print("######################")

while(42):
    order = input("Order : ")

    core.processOrder(order)

    print("\n--------------\n")