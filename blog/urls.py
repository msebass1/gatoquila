from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/users',views.usr_registro ,name='usr_registro'),
    path('post/', views.post_detail , name='post_detail'),
    # asigna un int a la variable pk 
    path('contacto/new/', views.post_new , name='post_new'),
    path('adopcion/', views.adopcion ,name='adopcion'),
    path('blog/', views.blog, name='blog'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('adopcion/formas',views.form_gato, name='form_gato'),
    path('blog/form', views.form_articulo, name='form_articulo')
]