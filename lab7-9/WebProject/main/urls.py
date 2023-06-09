from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('change_table/', views.change_table),
    path('edit/<int:id>', views.edit),
    path('remove/<int:id>', views.remove),
    path('append/', views.add_new)
]