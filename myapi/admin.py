from django.contrib import admin
from .models import *

# Register your models here.
models = [Owner,Room,HH]

for model in models:
    admin.site.register(model)

