from drf_yasg import openapi
from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status as rest_status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, TokenSerializer, StartapperSerializer, IdeaSerializer, StaffSerializer, \
    ApplicationStaffSerializer, SuccessProjectSerializer, CommentSerializers
from basic.models import CustomUser, Startapper, IdeaStartapper, Staff, ApplicationStaff, SuccessProject
from .pagination import CustomPagination



class UserList(ModelViewSet):
    serializer_class = UserSerializer
    print(UserSerializer, '+++++++++++++++++++++++++++++++++')
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    pagination_class = CustomPagination

    def get_serializer_context(self):
        return {'request': self.request}


class TokenGenerateView(TokenObtainPairView):
    serializer_class = TokenSerializer
    print(TokenSerializer, '+++++++++++++++++++++++++++++++++')
    post_responses = {
        rest_status.HTTP_201_CREATED: openapi.Response(description='Token obtained'),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description='User not found'),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(description='Validation error'),
    }

    def get_serializer_context(self):
        return {'request': self.request}



class SuccessProjectViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = SuccessProject.objects.all()
    serializer_class=SuccessProjectSerializer

class CommentViewSet(ModelViewSet):
    queryset = SuccessProject.objects.all()
    serializer_class = CommentSerializers

class ApplicationStaffViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ApplicationStaff.objects.all()
    serializer_class = ApplicationStaffSerializer

    # def get_serializer_context(self):
    #     return {'request': self.request}


class IdeaViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = IdeaStartapper.objects.all()
    serializer_class = IdeaSerializer


class StaffViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StartapperViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Startapper.objects.all()
    serializer_class = StartapperSerializer

