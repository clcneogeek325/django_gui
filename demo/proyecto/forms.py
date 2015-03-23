from django import forms
from .models import proyecto
from django.contrib.auth.models import User

class formProyecto(forms.ModelForm):
	#user = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=forms.TextInput(attrs={'type': 'hiden'}))
	nombre = forms.CharField(label="Nombre:",widget=forms.TextInput(attrs={'class': 'form-control','aria-describedby':'helpBlock'}))
	class Meta:
		model = proyecto
		fields = {'nombre',}
