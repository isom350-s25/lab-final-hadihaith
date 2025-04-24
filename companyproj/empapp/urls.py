from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("show_employees/", views.show_employees, name="show_employees"),
    path('employee_record/<int:id>/', views.employee_record, name='employee_record'),
    path('employee_stat/', views.employee_stat, name='employee_stat'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
]
