from django.urls import path
from .views import index, register, login_user, logout_user, announcement, announcementView, announcement_delete, \
    Startapper_update, developer_home, startapper_home, practitioner_home, AllUserIdea, Developer_update, AnnouncementUpdate#, AllUserUpdate

urlpatterns = [
    path('', index, name='home'),
    path('announcement/', announcement, name='announcement'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    #path('account/update/', AllUserUpdate.as_view(), name='all_user_update'),
    path('developer/', developer_home, name='developer'),
    path('developer/update/', Developer_update.as_view(), name='developer_update'),
    path('startapper/', startapper_home, name='startapper'),
    path('practitioner/', practitioner_home, name='practitioner'),
    path('startapper/update/', Startapper_update.as_view(), name='startapper_account'),
    path('announcement/<int:pk>/', announcementView.as_view(), name='idea_detail_startapper'),
    path('<int:pk>/edit/', AnnouncementUpdate.as_view(), name='announcement_update'),
    # path('staff-idea/', alluseridea, name='alluseridea'),
    path('allideasave/', AllUserIdea.as_view(), name='ideasave'),
    path('<int:id>/delete/', announcement_delete, name='ann-delete'),

]
