

class Map:
	def __init__(self) -> None:
		self._cities =  []

	def add_city(self, c):
		self._cities.append(c)
		return c
	
	def print(self):
		ret = ""
		for c in self._cities:
			if ret != "":
				ret += "; "
			ret += c.print()
		return ret

class City:
	def __init__(self, name) -> None:
		self._name = name
		self._schools = []
		
	def add_school(self, school):
		self._schools.append(school)

	def print(self):
		ret = ""
		for s in self._schools:
			if ret != "":
				ret += ", "
			ret += "(" + s.print() + ")"
		return self._name + " => " + ret

class School:
	def __init__(self, name) -> None:
		self._name = name
		
	def print(self):
		pass

class University(School):
	def __init__(self, name) -> None:
		super().__init__(name)

	def print(self):
		return self._name + ", University"

class HighSchool(School):
	def __init__(self, name, language) -> None:
		super().__init__(name)
		self._language = language

	def print(self):
		return self._name + ", HighSchool, " + self._language


"""
	Add necessary code so that, when we run the program, the following output is generated. Do not change the given code. 
	All your code should be written in classes. Use polymorphism as much as possible.

Istanbul => (BU, University), (ITU, University), (DSI, HighSchool, German), (GS, HighSchool, French); Konya => (Selcuk, University), (KAL, HighSchool, English)
"""

def Run():
	m = Map();
	C1 = m.add_city(City("Istanbul"));
	C2 = m.add_city(City("Konya"));

	C1.add_school(University("BU"));
	C2.add_school(University("Selcuk"));
	C1.add_school(University("ITU"));
	C1.add_school(HighSchool("DSI", "German"));
	C1.add_school(HighSchool("GS", "French"));
	C2.add_school(HighSchool("KAL", "English"));

	return m.print();