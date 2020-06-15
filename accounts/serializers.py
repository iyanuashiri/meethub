from djoser import serializers
from rest_framework import serializers as serialize

from .models import Account


class AccountSerializer(serializers.UserSerializer):
    url = serialize.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')

    class Meta:
        model = Account
        fields = ('id', 'url', 'email', 'first_name', 'last_name',)
        read_only_fields = ('id', 'email',)
