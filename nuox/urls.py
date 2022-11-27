from django.urls import path
from .import views


urlpatterns=[


path('login',views.login,name='login'),
path('sign',views.sign,name='sign'),
path('welcome',views.welcome,name='welcome'),
path('staffs',views.staffs,name='staffs'),
path('show_staff',views.show_staff,name='show_staff'),
path('edit_staff/<int:id>',views.edit_staff,name='edit_staff'),
path('update_staff/<int:id>',views.update_staff,name='update_staff'),
path('delete_staff/<int:id>',views.delete_staff,name='delete_staff'),
path('logout',views.logout,name='logout'),
path('item',views.item,name='item'),









]