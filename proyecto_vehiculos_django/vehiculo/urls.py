from django.urls import path
from .views import index, vehiculoform_view, vehiculolist_view, CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path("", index, name = "index" ),
    path("vehiculo/add/", vehiculoform_view, name="add_vehiculo"),    
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("accounts/logout/", CustomLogoutView.as_view(), name="logout"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("vehiculo/list/", vehiculolist_view, name="list_vehiculo"),
]