from django.contrib import admin
from django.urls import path, include
from myproject import views
from django.conf import settings
from django.conf.urls.static import static

app_name= "myproject"

urlpatterns = [
	path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
	path('account/', include('accounts.urls', namespace='accounts')),
	path('home/', include('home.urls', namespace='home')),	
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
