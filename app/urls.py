from django.urls import path
from .views import home, contacto, productos

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('productos/', productos, name="productos"),
]