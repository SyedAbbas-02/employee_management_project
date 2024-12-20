from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employee/list/', views.employee_list, name='employee_list'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
] 