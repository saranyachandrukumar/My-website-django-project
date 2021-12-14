from django.urls import path
from.import views


urlpatterns = [
    path('', views.Home),
    path('index/', views.index, name='index'),
    path('gallery/', views.gallery),
    path('products/', views.products),
    path('Contact/', views.Contact),
    path('aboutus/', views.aboutus),

]