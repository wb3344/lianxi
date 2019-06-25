from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('nv', views.NewView.as_view(), name='nv'),
    path('new/', views.new, name='new'),
    path('tiyu/', views.tiyu, name='tiyu'),
]
