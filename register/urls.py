from django.urls import path
from register import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('intro.html', views.intro),
    path('service.html', views.service),
    path('blog.html', views.blog),
    path('contact.html', views.contact),
    path('login.html', views.login),
    path('signin.html', views.signin),
    path('logout.html', views.logout),
    path('changepass', views.changepassword, name='changepass'),
]
