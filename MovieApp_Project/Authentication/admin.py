from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from Authentication.models import User, Profile


admin.site.register(User)
admin.site.register(Profile)
