from django.urls import path
from . import views
app_name = 'practest'

urlpatterns =[
    path('', views.record_list,name = 'record_list'),
    path('add', views.person_add, name='person_add'),
    path('edit', views.person_update, name='person_update'),
    path('delete', views.person_delete, name='person_delete'),
]