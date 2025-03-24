file_to_test = "question.py"

def test_4():

	with open(file_to_test) as f:
		ls = f.readlines()

		foundClass = False
		for l in ls:
			if l.count("class City:") == 1:
				foundClass = True
				continue

			if foundClass and l.count("class ") > 0:
				assert False, "City class does not have a function called add_school"
			
			if foundClass and l.count("def add_school"):
				assert True
				return

	assert False, "City class does not have a function called add_school"
