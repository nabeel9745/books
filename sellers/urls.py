from unicodedata import name
from django.urls import path
from.import views

urlpatterns=[
    path('ajax',views.ajax,name='ajax'),
    path('aj',views.aj,name='aj'),
    # path('show',views.show,name='show'),
    path('dele',views.dele,name='dele'),
    path('upd',views.upd,name='upd'),
    path('submit',views.submit,name='submit'),
    path('camel',views.camel,name='camel'),
    path('input_camel',views.input_camel,name='input_camel'),
    path('camelwrk',views.camelwrk,name='camelwrk'),
    path('p_view',views.p_view,name='p_view'),
    # //
    path('otp',views.otp,name='otp'),
    path('welcome',views.welcome,name='welcome'),
    path('re',views.re,name='re'),
    path('info',views.info,name='info'),
    path('log_a',views.log_a,name='log_a'),











    



]