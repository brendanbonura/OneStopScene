from django import forms
from home.models import Post
from datetime import date

class HomeForm(forms.ModelForm):
	EVENTCHOICES = (('Concert', 'Concert'),('Party', 'Party'),('Seminar', 'Seminar'),('Sports', 'Sports'),('Gaming', 'Gaming'),('Other', 'Other'))
	title = forms.CharField()
	image = forms.ImageField()
	description = forms.CharField()
	event_type = forms.ChoiceField(choices = EVENTCHOICES)
	date = forms.DateField(input_formats = ['%Y-%m-%d'],initial=date.today)
	location = forms.CharField()
	
	class Meta:
		model = Post
		fields =('title', 'image', 'description', 'event_type', 'date', 'location',)