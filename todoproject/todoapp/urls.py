from django.contrib import admin
from django.urls import path, include

from todoapp import views
app_name='todoapp'

urlpatterns = [
    path('',views.index, name='index'),
    path('details/',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cv/',views.TasklistView.as_view(),name='cv'),
    path('cvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cvdetail'),
    path('cvupdate/<int:pk>/',views.TaskuodateView.as_view(),name='cvupdate'),
    path('cvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cvdelete'),



]
