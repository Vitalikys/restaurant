import datetime

from django.shortcuts import render
from rest_framework import viewsets, generics, versioning
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from api.serializers import UserSerializer, MenuSerializer, OrderSerializer
from menu.models import Menu, Order
from menu.service import get_client_ip
from restaurant_user.models import RestaurantUser


class RastaurantVersioning(versioning.AcceptHeaderVersioning):
    allowed_versions = ('1.0', '2.0')
    default_version = '2.0'
    # version_param =
    invalid_version_message = 'wrong version, try again'


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
    """ Get all week menu """
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = (IsAdminUser,)


class MenuCreateView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = (IsAdminUser,)


class MenuRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = (IsAdminUser,)


class OrderCreateView(generics.CreateAPIView):
    versioning_class = RastaurantVersioning
    # versioning_class = versioning.QueryParameterVersioning
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)

    # class OrderCreateView(viewsets.ModelViewSet):
    #  ''' partial_update,  '''
    #     serializer_class = OrderSerializer
    #     queryset = Order.objects.all()
    #     permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        print('my user id is:', self.request.user.id)
        print('request version: ', self.request.version)
        serializer.save(ip=get_client_ip(self.request),
                        user=self.request.user)


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = OrderSerializer
    versioning_class = RastaurantVersioning


class OrderDestroyView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = OrderSerializer
    versioning_class = RastaurantVersioning

