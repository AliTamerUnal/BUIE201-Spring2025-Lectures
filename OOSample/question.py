
# Add your code before this line. Do not change the code below this line.

def Run():
	m = Map()
	C1 = m.add_city(City("Istanbul"))
	C2 = m.add_city(City("Konya"))

	C1.add_school(University("BU"))
	C2.add_school(University("Selcuk"))
	C1.add_school(University("ITU"))
	C1.add_school(HighSchool("DSI", "German"))
	C1.add_school(HighSchool("GS", "French"))
	C2.add_school(HighSchool("KAL", "English"))

	return m.print()


print (Run())