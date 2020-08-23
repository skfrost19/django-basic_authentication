from django.urls import path
from firstwebapp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('signup2/', views.signup2, name='signup2'),
    path('signin/', views.signin,name='signin'),
    path('contact/', views.ContactUs,name='contact'),
    path('about/', views.AboutUs,name='about'),

]
