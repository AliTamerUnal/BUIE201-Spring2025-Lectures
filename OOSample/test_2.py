file_to_test = "question.py"

def test_2():

	with open(file_to_test) as f:
		all = f.read()

		assert all.count("class ") > 4, "Solution has less than 5 classes."
		return	
	