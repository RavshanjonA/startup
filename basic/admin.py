from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import *

admin.site.register(ApplicationStaff)


@admin.register(SuccessProject)
class SuccessProjectsAdmin(TranslatableAdmin):
    list_display = ('title', 'description',)


# admin.site.register(SuccessProjects)
admin.site.register(CommentOfPost)

@admin.register(AboutUS)
class AboutUSAdmin(TranslatableAdmin):
    list_display = ('post_title', 'post_description',)

admin.site.register(ContactsProwork)

@admin.register(ProworkAdress)
class ProworkAdressAdmin(TranslatableAdmin):
    list_display = ('branch_name',)

