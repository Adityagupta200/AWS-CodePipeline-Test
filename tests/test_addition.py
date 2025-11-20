from tests.my_module import add

def test_add_positive_numbers(a, b):
	assert add(2, 3) == 5

def test_add_negative_numbers(a, b):
	assert add(-2,- 3) == -5
