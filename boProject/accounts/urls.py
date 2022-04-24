
from django.urls import path
from accounts import views

urlpatterns = [

 path('login/',views.login_view),
 path('logout/',views.logout_view),
 path('user',views.UserView.as_view(), name='user'),
 path('user/<str:pk>',views.details)
]
