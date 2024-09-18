from django.urls import path
from djangoIntroduction.to_do_app import views


urlpatterns = [
    path('', views.index, name='index'),
]