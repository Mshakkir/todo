
from django.contrib import admin
from django.urls import path, include

from todoapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/', views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDetailview.as_view(), name='cbvdelete')
]
