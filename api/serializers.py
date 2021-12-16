from rest_framework import serializers
from basic.models import CustomUser
# from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from basic.models import Startapper, IdeaStartapper, Staff, ApplicationStaff, SuccessProject, CommentofPost



class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data.get('password1') and data.get('password2'):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError('Passwords must match!')
        return data

    def create(self, validated_data):
        print(validated_data)
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']
        data['username'] = validated_data['username']
        user = self.Meta.model.objects.create_user(**data)
        user.is_active = True
        user.save()

        return user

    class Meta:
        model = CustomUser
        exclude = ['password', 'is_superuser', 'user_permissions', 'groups', 'date_joined', 'first_name', 'last_name']
        read_only_fields = ('last_login', 'is_staff', 'is_superuser', 'is_active')
        write_only_fields = ('password1', 'password2')


class TokenSerializer(TokenObtainPairSerializer):

    # @classmethod
    # def get_token(cls, user):
    #     token = super(TokenSerializer, cls).get_token(user)
    #     print(token,'+++++++++++++++++++++')
    #     # Add custom claims
    #     token['username'] = user.username
    #     return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # data['user'] = UserSerializer(instance=self.user, context=self.context).data
        return data



class CommentCreateSerializers(serializers.ModelSerializer):
    # post = SuccessProjectSerializer()

    class Meta:
        model = CommentofPost
        fields = "__all__"
        # fields = ('post', 'replay_to', 'owner', 'comment', )


class SuccessProjectSerializer(serializers.ModelSerializer):
    # commit = CommentCreateSerializers()

    class Meta:
        model = SuccessProject
        fields = ('id', 'title', 'description', 'image', 'url',)

    # def create(self, validated_data):
    #     return SuccessProject.objects.create(**validated_data)
    #
    # def update(self, instance, validated_date):
    #     instance.title = validated_date.get('title', instance.title)
    #     instance.description = validated_date.get('description', instance.description)
    #     instance.image = validated_date.get('image', instance.image)
    #     instance.url = validated_date.get('url', instance.url)
    #     instance.save()
    #     return instance


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Staff
        fields = ('id', 'user', 'bio', 'country', 'image')


class ApplicationStaffSerializer(serializers.ModelSerializer):
    user = StaffSerializer()

    class Meta:
        model = ApplicationStaff
        fields = ('user', 'title', 'description', 'resume', 'work_type')


class StartapperSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Startapper
        fields = ('id', 'user', 'bio', 'country', 'image')

class IdeaSerializer(serializers.ModelSerializer):
    user = StartapperSerializer()

    class Meta:
        model = IdeaStartapper
        fields = ('user', 'title', 'description', 'file')




class UserReg(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name')

