from django.urls import path
from .import views



urlpatterns =[
           path('',views.studentreg,name='studentreg'),
           path('read/',views.read,name='read'),
           path('delete/<str:pk>',views.delete,name='delete'),
           path('update/<str:pk>',views.update,name='update'),
           path('login/',views.login,name='login'),
           path('welcome/',views.welcome,name='welcome'),
           path('userlog/',views.userlog,name='userlog'),

]