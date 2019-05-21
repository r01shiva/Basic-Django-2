from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

    path('',views.main,name='main'),

    path('about/',views.about,name='about'),

    path('contact/',views.contact,name='contact'),

    url(r'^product/$',views.IndexViewPro.as_view(),name='product'),

    url(r'^product/(?P<pk>[0-9]+)/$',views.DetailViewPro.as_view(),name='detailp'),

    url(r'^buynow/$', views.buynow, name='buynow'),

    url(r'^product2/$', views.product2, name='proo'),

]
