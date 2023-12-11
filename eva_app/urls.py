from django.urls import path

from eva_app import views

urlpatterns = [
    path('',views.work1,name='new'),
    path('page1',views.view,name='new1'),
    path('page2',views.create,name='new2'),
    path('page3',views.update,name='new3'),
    path('update/<int:id>/',views.update,name='new4'),
    path('delt1/<int:id>/',views.delt,name='delt1')

]