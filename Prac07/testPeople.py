from people import Address, Person, Staff, Student, Postgrad, Undergrad

print('#### People Test Program ###')

testAdd = Address('10', 'Downing St', 'Carlisle', '6101')
testPerson = Person('Winston Churchill', '30/11/1874', testAdd)
testPerson.displayPerson()
print()

#Question3 = Add in another test person and re-run the program.
#testAdd = Address('19', 'Barrack St', 'Perth', '6000')
#testPerson = Person('June', '7/7//1977', testAdd)
#testPerson.displayPerson()


testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
testPerson2 = Staff('Professor Awesome', '1/6/61', testAdd2, '12345J')
testPerson2.displayPerson()
print()


testAdd3 = Address('2', 'Bassendean', 'Perth', '6012')
testPerson3 = Student('June', '6/11/1996', testAdd3, '22222A')
testPerson3.displayPerson()
print()


testAdd4 = Address('3', 'East Perth', 'Perth', '6003')
testPerson4 = Postgrad('Tabitha', '2/5/1990', testAdd4, '33333B')
testPerson4.displayPerson()
print()

testAdd5 = Address('4', 'West Perth', 'Perth', '6002')
testPerson5 = Undergrad('Taku', '1/1/1988', testAdd5, '44444C')
testPerson5.displayPerson()
print()
