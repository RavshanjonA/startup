from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('Users', UserList)
router.register('Startapper', StartapperViewSet)
router.register('Staff', StaffViewSet)
router.register('Idea startapper', IdeaViewSet)
router.register('Application Staff', ApplicationStaffViewSet)
router.register('Success Project', SuccessProjectViewSet)

urlpatterns = router.urls + [
    path('token/', TokenGenerateView.as_view(), name='token_obtain_pair'),

]
