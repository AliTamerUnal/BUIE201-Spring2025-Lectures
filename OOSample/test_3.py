file_to_test = "question.py"

def test_3():

	with open(file_to_test) as f:
		ls = f.readlines()

		foundClass = False
		for l in ls:
			if l.count("class Map:") == 1:
				foundClass = True
				continue

			if foundClass and l.count("class ") > 0:
				assert False, "Map class does not have a function called add_city"
			
			if foundClass and l.count("def add_city"):
				assert True
				return

	assert False, "Map class does not have a function called add_city"
