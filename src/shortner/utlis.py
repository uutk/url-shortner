import random
import string

def get_shortcode(size = 6, char = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(char) for _ in range(size))

def create_shortcode(instance, size=6):
	new_code = get_shortcode(size=size)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code