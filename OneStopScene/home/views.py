from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.forms import HomeForm
from home.models import Post, Connection
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.models import User

class HomeView(TemplateView):
	template_name = 'home/home.html'
	
	def get(self, request):
		form = HomeForm()
		yesterday = datetime.now() - timedelta(days=1)
		posts = Post.objects.all().filter(date__gte=yesterday).order_by('date')
		users = User.objects.exclude(id=request.user.id)
		try:
			connection = Connection.objects.get(current_user = request.user)
			connections = connection.users.all()
		except Connection.DoesNotExist:
			connections = None
		
		args = {'form': form, 'posts': posts, 'users': users, 'connections': connections}
		return render(request, self.template_name, args)
		
	def post(self, request):
		form = HomeForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit = False)
			post.user = request.user
			post.save()
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			date = form.cleaned_data['date']
			event_type = 'event_type'
			location = form.cleaned_data['location']
			image = form.cleaned_data['image']
			form = HomeForm()
			return redirect('home:home')
		else:
			messages.info(request, 'The post you tried to submit was invalid. Please make sure you have chosen an image and the date is correctly formatted as yyyy-mm-dd')
			return redirect('home:home')
			
		args = {'form': form, 
				'title': title, 
				'description': description,
				'date': date,
				'event_type': event_type,
				'location': location,
				'image': image,
		}
		return render(request, self.template_name, args)

def change_connections(request, operation, pk):
	connection = User.objects.get(pk=pk)
	if operation == 'add':
		Connection.make_Connection(request.user, connection)
	elif operation == 'remove':
		Connection.lose_Connection(request.user, connection)
	return redirect('home:home')