from django.urls import path

from . import views
urlpatterns = [
    
    path('',views.Home, name='Home'),
    path('token',views.token_send, name="token_send"),
    path('userdetail',views.userdetail, name='userdetail'),
    path('verify/<auth_token>',views.verify, name='verify'),
    path('error', views.error, name='error'),
    path('login1', views.login1, name='login1'),
    path('Logout',views.Logout,name='Logout'),
    path('About',views.About,name='About'),
    path('contact',views.contact,name='contact'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('profile',views.profile,name='profile'),
    path('uprofile',views.uprofile,name='uprofile'),
    path('forgot',views.forgot,name='forgot'),
    path('fpassword',views.fpassword,name='fpassword'),
    path('forpassword',views.forpassword,name='forpassword'),
    path('pass1',views.pass1,name='pass1'),
    path('add-contact', views.addContact, name='add-contact'),
    path('edit-contact/<str:pk>', views.editContact, name='edit-contact'),
    path('delete/<str:pk>', views.deleteContact, name='delete'),
    path('contactprofile/<str:pk>', views.contactProfile, name='contactprofile')
]
