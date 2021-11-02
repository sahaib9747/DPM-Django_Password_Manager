from django.urls import path
print('This is manager.urls')
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]

