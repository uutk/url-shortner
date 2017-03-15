from django import forms 
from .validators import validate_url,validate_dot_com

class SubmitURL(forms.Form):
	url = forms.CharField(
			label='', 
			validators=[validate_url,validate_dot_com,],
			widget = forms.TextInput(
				attrs={
					"placeholder": "URL",
					"class":"form-control"
					}
				)
			)

	"""def clean_url(self):
					url = self.cleaned_data['url']
					if "https://" in url  or "http://" in url:
						return url
					else:
						return "https://" + url	"""