from django.forms import ModelForm
from .models import destination,posted


class tegisterForm(ModelForm):
	class Meta:
		model = destination
		fields = '__all__'
		exclude = ['user']

class postForm(ModelForm):
	class Meta:
		model = posted
		fields = '__all__'
		exclude = ['user']

