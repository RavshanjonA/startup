from django.urls import path
from .views import index, register, login_user, logout_user, startapper_account, announcement,announcementView

urlpatterns = [
    path('', index, name='home'),
    path('announcement/', announcement, name='announcement'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('startapper/', startapper_account, name='startapper_account'),
    path('announcement/<int:pk>/', announcementView.as_view(), name='idea_detail_startapper'),

]
