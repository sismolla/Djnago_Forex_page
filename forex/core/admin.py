from django.contrib import admin
from .models import Forex


@admin.register(Forex)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
