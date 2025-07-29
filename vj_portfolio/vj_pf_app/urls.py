from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = 'portfolio.views.custom_404_view'

urlpatterns = [
    # path('index/',views.index),
    path('', views.contact_form, name='contact_form'),
]