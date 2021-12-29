from django.contrib import admin

from .models import User, Guild

# Register your models here.

admin.site.register(User)
admin.site.register(Guild)