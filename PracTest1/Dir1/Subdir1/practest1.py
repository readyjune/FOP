#
# Student Name : jinwookim
# Student ID   : 90021907
#
# practest1.py - Read in a string and print it
#
instring = input("Enter a string... ")
instring = instring.upper()
print('The string is : ', instring)

#reversing with a range loop


for index in range(0, len(instring)-1, 2):
    print(instring[index], end='')
print()


for index in range(1, len(instring), 3):
    print(instring[index], end='')
print()

