from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField

class Post(models.Model):
	title = models.CharField(max_length=150)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profile_image', blank=True)
	description = models.CharField(max_length=500)
	date = models.DateTimeField()
	EVENT_TYPE_CHOICES =(
		('Concert', 'Concert'),
		('Party', 'Party'),
		('Seminar', 'Seminar'),
		('Sports', 'Sports'),
		('Gaming', 'Gaming'),
		('Other', 'Other')
	)
	event_type = models.CharField(max_length=10, choices = EVENT_TYPE_CHOICES, default = 'other')
	location = models.CharField(max_length=150)	
	
class Connection(models.Model):
	users = models.ManyToManyField(User)
	current_user = models.ForeignKey(User, related_name='owner', null = True, on_delete=models.CASCADE)
	
	@classmethod
	def make_Connection(cls, current_user, new_connection):
		connection, created = cls.objects.get_or_create(
			current_user = current_user
		)
		connection.users.add(new_connection)
		
	@classmethod
	def lose_Connection(cls, current_user, new_connection):
		connection, created = cls.objects.get_or_create(
			current_user = current_user
		)
		connection.users.remove(new_connection)