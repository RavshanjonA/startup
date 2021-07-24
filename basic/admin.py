from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.contrib.auth.models import AbstractUser
from .models import *

admin.site.register(
    [CustomUser, Country, Startapper, Staff, IdeaStartapper, AllUsersIdea, ApplicationStaff, ContactsProwork,
     CommentofPost])


@admin.register(SuccessProject)
class SuccessProjectsAdmin(TranslatableAdmin):
    list_display = ('title', 'description',)


@admin.register(AboutUS)
class AboutUSAdmin(TranslatableAdmin):
    list_display = ('post_title', 'post_description',)


@admin.register(ProworkAdress)
class ProworkAdressAdmin(TranslatableAdmin):
    list_display = ('branch_name',)

