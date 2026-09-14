from django.contrib import admin

# Register your models here.
from .models import Mahasiswa, Interest, Education, Experience

admin.site.register(Mahasiswa)
admin.site.register(Interest)
admin.site.register(Education)
admin.site.register(Experience)
