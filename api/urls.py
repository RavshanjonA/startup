from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('users', UserList)
router.register('startapper', StartapperViewSet)

urlpatterns = router.urls + [
    path('token/', TokenGenerateView.as_view(), name='token_obtain_pair'),

]