from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *
# Register your models here.

admin.site.register(CustomUser)


admin.site.register(Country)

admin.site.register(Staff)

admin.site.register(IdeaStartapper)

admin.site.register(AllUsersIdea)

admin.site.register(ApplicationStaff)

@admin.register(SuccessProject)
class SuccessProjectsAdmin(TranslatableAdmin):
    list_display = ('title', 'description',)


# admin.site.register(SuccessProjects)
admin.site.register(CommentOfPost)

@admin.register(AboutUS)
class AboutUSAdmin(TranslatableAdmin):
    list_display = ('post_title', 'post_description',)

admin.site.register(ContacktsProwork)
admin.site.register(ProworkAdress)