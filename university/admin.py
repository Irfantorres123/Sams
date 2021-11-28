from django.contrib import admin

from university.models import University

# Register your models here.
admin.site.site_header = "University Administration"
admin.site.site_title = "University Administration Portal"
admin.site.index_title = "Welcome to the University Administration Portal"

admin.site.register(University)
