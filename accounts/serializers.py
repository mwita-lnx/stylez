from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Vendor,Customer
User = get_user_model()



#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )

  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)


  class Meta:
    model = User
    fields = ('password', 'password2','email','name')
    extra_kwargs = {
      'name': {'required': True},
      'email': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      email=validated_data['email'],
      name=validated_data['name'],

    )
    user.set_password(validated_data['password'])
    user.save()
    return user

class UserActivation(serializers.Serializer):
    token = serializers.CharField()
    email= serializers.CharField()
    mode = serializers.CharField()

class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError("Incorrect old password")
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance



class VendorSerializer(serializers.ModelSerializer):
  user= serializers.PrimaryKeyRelatedField(source='user.id',read_only=True)
  profile_pic = serializers.ImageField(required=False)
  class Meta:
    model = Vendor
    fields = ['user', 'location', 'description', 'contact_no', 'product_categories','comission_rate','profile_pic']


class CustomerSerializer(serializers.ModelSerializer):
  user= serializers.PrimaryKeyRelatedField(source='user.id',read_only=True)
  class Meta:
    model = Customer
    fields = "__all__"

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.HyperlinkedModelSerializer):

  customer = CustomerSerializer(many=False, read_only=True)
  vendor = VendorSerializer(many=False, read_only=True)

  class Meta:
    model = User
    fields = ["id", "email", "name","customer","vendor"]
