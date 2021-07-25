from rest_framework import serializers
from basic.models import CustomUser
# from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from basic.models import Startapper, IdeaStartapper, Staff, ApplicationStaff, SuccessProject


class SuccessProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessProject
        fields = ('title', 'description', 'image', 'url')


class ApplicationStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStaff
        fields = ('user', 'title', 'description', 'resume', 'work_type')


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaStartapper
        fields = ('user', 'title', 'description', 'file')


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('user', 'bio', 'country', 'image')


class StartapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startapper
        fields = ('user', 'bio', 'country', 'image')


class UserReg(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name')


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data.get('password1') and data.get('password2'):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError('Passwords must match.')
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
        user.is_active = False
        user.save()

        return user

    class Meta:
        model = CustomUser
        exclude = ['password', 'is_superuser', 'user_permissions', 'groups', 'date_joined', 'first_name', 'last_name']
        read_only_fields = ('last_login', 'is_staff', 'is_superuser', 'is_active')
        write_only_fields = ('password1', 'password2')


class TokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = UserSerializer(instance=self.user, context=self.context).data
        return data
