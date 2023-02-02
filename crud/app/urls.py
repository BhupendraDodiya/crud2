from django.urls import path,re_path
from app import views

urlpatterns = [
    path('',views.index),
    path('reg/',views.registration),
    path('login/',views.login),
    path('log_detail/',views.log_detail),
    path('table/',views.table),
    path('update/<int:uid>/',views.update),
    path('update_form/',views.update_form),
    re_path(r'^delete/(?P<pk>[0-9]+)/$',views.delete_form,name='del')
]