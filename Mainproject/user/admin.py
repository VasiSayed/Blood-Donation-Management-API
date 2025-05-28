from django.contrib import admin
from .models import User,Patient,Donation

admin.site.register([User,Patient,Donation])
