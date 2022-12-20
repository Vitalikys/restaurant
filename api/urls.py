from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import *
# from api.views import UserViewSet, MenuTodayListView, MenuCreateView, \
#     MenuAllWeekListView, OrderCreateView, MenuRetrieveUpdateView, OrderListView

router = DefaultRouter()
router.register(r'user', UserViewSet)
# router.register(r'order', OrderCreateView, basename='order')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include(router.urls)),
    path('menu/', MenuCreateView.as_view()),
    path('menu/<int:pk>/', MenuRetrieveUpdateView.as_view()),
    path('menu_for_today/', MenuTodayListView.as_view()),
    path('menu_all_week/', MenuAllWeekListView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    path('order/list/', OrderListView.as_view()),
    path('order/list_current_day/', OrderCurrentDayListView.as_view()),
    path('order/delete/<int:pk>/', OrderDestroyView.as_view()),

]
