from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
	url_validator = URLValidator()
	value_0_invalid = False
	value_1_invalid = False
	
	try :
		url_validator(value)
	except:
		value_0_invalid = True

	value_1 = "https://" + value

	try :
		url_validator(value_1)
	except:
		value_1_invalid = True

	if value_0_invalid and value_1_invalid:
		raise ValidationError("Invalid URL")
	
	return value

def validate_dot_com(value):
	if not ".com" in value or not ".in" in value:
		raise ValidationError("Invalid URL")
	return value	


