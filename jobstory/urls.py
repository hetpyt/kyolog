from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('form_test', views.form_test, name='form_test')
]
