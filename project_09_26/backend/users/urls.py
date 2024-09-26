from django.urls import path

from users.views import UserCreateView, CurrentUserApiView, UserListApiView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('list/', UserListApiView.as_view()),
    path('<int:pk>/', CurrentUserApiView.as_view())
]