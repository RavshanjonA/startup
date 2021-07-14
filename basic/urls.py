from django.urls import path
from .views import index, register, login_user, logout_user, announcement, announcementView, announcement_delete, \
    startapper_update, developer_home, startapper_home, practitioner_home

urlpatterns = [
    path('', index, name='home'),
    path('announcement/', announcement, name='announcement'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('developer/', developer_home, name='developer'),
    path('startapper/', startapper_home, name='startapper'),
    path('practitioner/', practitioner_home, name='practitioner'),
    path('startapper/', startapper_update.as_view(), name='startapper_account'),
    path('announcement/<int:pk>/', announcementView.as_view(), name='idea_detail_startapper'),
    path('<int:id>/delete/', announcement_delete, name='ann-delete'),

]
