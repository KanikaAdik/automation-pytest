

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


def str_to_bool(val):
	true_vals=['yes','y','']
	false_vals =['no', 'n']
	try:
		val = val.lower()
	except AttributeError:
		val = str(val).lower()
	if val in true_vals:
		return True
	elif val in false_vals:
		return False
	else:
		raise ValueError("invalid input value %s"%val)
