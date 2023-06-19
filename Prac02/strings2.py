#
# strings1.py: Read in a string and print it in reverse
#              using a loop and a method call

instring = input('Enter a string... ')
# *** and upper and duplicating code here

mokpo = instring.upper()
print(mokpo)

mokpo = mokpo + mokpo
print(mokpo)

# reversing with a while loop

print('Reversed string is : ', end='')
index = 0
while index <= len(instring)-1:
    print(instring[index], end='')
    index = index + 1
print()

# reversing with a range loop

print('Reversed string is : ', end='')
for index in range(0, len(instring), 1):
    print(instring[index], end='')
print()

# reversing with slicing

print('Reversed string is :', instring[::1])




# reversing with a while loop

print('Reversed string is : ', end='')
index = 0
while index <= len(instring)-1:
    print(instring[index], end='')
    index = index + 2
print()

# reversing with a range loop

print('Reversed string is : ', end='')
for index in range(0, len(instring), 2):
    print(instring[index], end='')
print()

# reversing with slicing

print('Reversed string is :', instring[::2])


# reversing with a while loop

print('Reversed string is : ', end='')
index = 1
while index <= len(instring)-2:
    print(instring[index], end='')
    index = index + 2
print()

# reversing with a range loop

print('Reversed string is : ', end='')
for index in range(1, len(instring)-1, 2):
    print(instring[index], end='')
print()

# reversing with slicing

print('Reversed string is :', instring[1:-1:2])
