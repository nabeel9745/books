
from xml.etree.ElementInclude import include
from django.urls import path
from .import views


# app_name='buyers'

urlpatterns=[
path('reg',views.reg),
path('seller',views.seller),
path('show',views.show,name="show"),
path('logout',views.logout,name="logout"),
path('login',views.login,name="login"),
path('product',views.product,name="product"),
path('p_show',views.p_show,name="p_show"),




# path('show3',views.show3,name="show3"),
# path('login',views.login,name="login"),
# path('show2',views.show2),
# path('delete/<int:id>',views.delete,name='delete'),
# path('update/<int:id>',views.update,name='update'),
# path('editing/int:id>',views.editing,name='editing')

]