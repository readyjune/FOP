#
# conversions.py - module with functions to convert between units
#
#	   fahr2cel : Convert from Fahrenheit to Celsius.
#
def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius.
	Argument:
	fahr = the temperature in Fahrenheit
	celsius = (fahr -32) * (5/9)
	"""
    celsius = (fahr - 32) * (5/9)
    return celsius

def cel2fahr(cel):
	fahrenheit = ( cel * 9/5) + 32
	return fahrenheit

def cel2kel(cel):
	"""Convert from Celsius to Kelvin.
	Argument:
	kelvin = celsius + 273.15
	"""
	kelvin = (cel + 273.15)
	return kelvin

def kel2cel(kel):
	celsius = (kel - 273.15)
	return celsius

def fahr2kel(fahr):
	kelvin = (fahr - 32) * 5/9 + 273.15
	return kelvin

def kel2fahr(kel):
	fahrenheit = (kelvin - 273.15) * 9/5 + 32
	return fahrenheit
