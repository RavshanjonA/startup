from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('users', UserList)
router.register('startapper', StartapperViewSet)
router.register('staff', StaffViewSet)
router.register('idea-startapper', IdeaViewSet)
router.register('application-staff', ApplicationStaffViewSet)
router.register('success-project', SuccessProjectViewSet)
router.register('commend-post', CommentViewSet)

urlpatterns = router.urls + [
    path('login/', TokenGenerateView.as_view(), name='token_obtain_pair'),

]
