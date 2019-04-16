from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  """ A serializer class for the User model """

  class Meta:
    # Specify the model we are using
    model = User
    # Specify the fields that should be made accessible.
    # Mostly it is all fields in that model
    fields = ('id', 'username',
              'password', 'is_active', 'is_superuser')
