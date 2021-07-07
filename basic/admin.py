from django.contrib import admin

admin.site.register(ApplicationStaff)

@admin.register(SuccessProjects)
class SuccessProjectsAdmin(TranslatableAdmin):
    list_display = ('title', 'description',)


# admin.site.register(SuccessProjects)
admin.site.register(CommentOfPost)

@admin.register(AboutUS)
class AboutUSAdmin(TranslatableAdmin):
    list_display = ('post_title', 'post_description',)

admin.site.register(ContacktsProwork)

@admin.register(ProworkAdress)
class ProworkAdressAdmin(TranslatableAdmin):
    list_display = ('branch_name',)

