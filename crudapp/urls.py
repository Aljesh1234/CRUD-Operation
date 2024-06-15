from django.contrib import admin
from django.urls import path,include
from . import views
# from employee.views import employee,index,update
urlpatterns = [
    path('',views.index),
    path('employee',views.employee, name='employee'),
    # path('update/<int:id>',views.update, name = 'update' )
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>',views.delete, name = 'delete'),
]