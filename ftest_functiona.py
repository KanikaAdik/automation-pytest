
def str_to_int(string):
	error_msg ="unable to convert o integr %s" % str(string)

	try:
		integer = float(string.replace(',', '.'))
	except AttributeError:
		if isinstance(string, (int,float)):
			integer = string
		else:
			raise RuntimeError(error_msg)
	except (TypeError, ValueError):
		raise RuntimeError(error_msg)
	return int(integer)

def test_rounds_down():
	result = str_to_int('1.99')
	assert result ==1

def test_rounds_down_lesser_half():
	result = str_to_int('1.2')
	assert result ==1
