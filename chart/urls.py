
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home,name='home'),
    path('add/', views.add,name='add'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('edited/<int:id>', views.edited),
    path('delete/<int:id>',views.delete),
]
