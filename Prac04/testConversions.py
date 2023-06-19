#
# testConversions.py - tests the functions in conversions.py
#
from conversions import fahr2cel
print("\nTESTING CONVERSIONS\n")
testF = 100
testC = fahr2cel(testF)
print("Fahrenheit is ", testF, " Celsius is ", testC)
print()



print(fahr2cel.__doc__)


from conversions import cel2kel
print("\nTESTING CONVERSIONS\n")
testC = 32
testK = cel2kel(testC)
print("Celsius is ", testC, " Kelvin is ", testK)
print()

print(cel2kel.__doc__)
