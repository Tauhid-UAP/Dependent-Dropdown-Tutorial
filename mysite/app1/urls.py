from django.urls import path

from . import views

urlpatterns = [
    path('personform_page/', views.personform_page, name='personform_page'),
]