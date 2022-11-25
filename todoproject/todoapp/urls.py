from . import views
from django.urls import path, include



urlpatterns = [

    path('',views.add,name='add'),
    path('detail',views.detail,name='detail'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvfront/',views.tlistview.as_view(),name='cbvfront'),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.taskupdateview.as_view(), name= 'cbvupdate'),
    path('cbvdelete/<int:pk>/', views.taskdeleteview.as_view(),name='cbvdelete')
]