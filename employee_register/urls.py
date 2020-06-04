from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list,name='list'),
    path('employee_form/', views.employee_form,name='insert_form'),
    path('<int:id>/', views.employee_form,name='update_form'),
    path('delete/<int:id>', views.employee_delete,name='delete'),
]