from django.contrib import admin
from accounts.models import UserProfile

admin.site.register(UserProfile)
admin.site.site_header = "OneStopScene Administration"
