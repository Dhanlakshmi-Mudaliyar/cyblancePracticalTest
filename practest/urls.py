from django.urls import path
from . import views

app_name = 'practest'

urlpatterns =[
    path('', views.record_list,name = 'record_list'),
    path('add', views.person_add, name='person_add'),
    path('edit/<int:id>', views.person_update, name='person_update'),
    path('delete/<int:id>', views.person_delete, name='person_delete'),
    path('register/', views.register_user, name='register1'),
    path('login/', views.user_login, name='login'),
    path('api/login/', views.user_login_api, name='login_api'),
    path('api/register',views.register_user_api,name="register_api")
]