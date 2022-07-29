from django.contrib import admin
from share.models import Category, Institution, Donation

admin.site.register(Category),
admin.register(Institution),
admin.site.register(Donation),
