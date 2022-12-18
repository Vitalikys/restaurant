from rest_framework import serializers

from menu.models import Menu, Order
from restaurant_user.models import RestaurantUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        write_only_fields = 'password'

    def create(self, validated_data):
        user = RestaurantUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('id', 'user', 'day_menu', 'created_at', 'ip')


