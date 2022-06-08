from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('todo/list/', views.ListAPIView.as_view(), name="list"),
    path('todo/<int:pk>/delete/', views.DeleteAPIView.as_view(), name="delete"),
    path('todo/create/', views.CreateAPIView.as_view(), name="create"),
]