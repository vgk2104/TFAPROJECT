from django.forms import ModelForm
from Squirrel.models import Squirrel

class SquirrelForm(ModelForm):
	class Meta:
		model = Squirrel
		fields = '__all__'
