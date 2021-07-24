from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('users', UserList)

urlpatterns = router.urls + [
    # path('ass', UserList.as_view()),
    path('token/', TokenGenerateView.as_view(), name='token_obtain_pair'),

]