from boApp import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('todo',views.TodoView.as_view(), name='todo'),
    path('todo/<int:pk>',views.TodoDetailsView.as_view(), name='TodoDetailsView')

]
