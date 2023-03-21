from django.urls import path

from . import views


app_name="remesas"
urlpatterns= [
    path('', views.index, name='index'),
    path('<int:usuarios_id>/', views.detail, name= 'detail')
]