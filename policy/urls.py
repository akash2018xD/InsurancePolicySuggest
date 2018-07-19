from django.urls import path
from . import views

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('details/',views.details.as_view(),name='details'),
    path('admin/',views.details.as_view(),name='admin'),
]
