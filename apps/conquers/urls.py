from django.conf.urls import url
from apps.conquers import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.user_login, name="login"),
    url(r'^logout$', views.user_logout, name="logout"),
    url(r'^actividad$', views.envio_actividad, name="activity")

]