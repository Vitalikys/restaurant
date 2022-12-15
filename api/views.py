import datetime

from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from api.serializers import UserSerializer, MenuSerializer, OrderSerializer
from menu.models import Menu, Order
from menu.service import get_client_ip
from restaurant_user.models import RestaurantUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = RestaurantUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class MenuTodayListView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        current_day = datetime.datetime.now()
        print('today is day: ', current_day.weekday())  # , current_day)
        return Menu.objects.filter(week_day=current_day.weekday())


class MenuAllWeekListView(generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = (IsAdminUser,)


class MenuCreateView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = (IsAdminUser,)


class OrderCreateView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        print('my user', self.request.user)
        serializer.save(ip=get_client_ip(self.request))
