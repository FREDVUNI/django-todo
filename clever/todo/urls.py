from django.urls import path
from . import views

urlpatterns = [
    path("",views.apiOverview,name="api"),
    path("task-list/",views.TaskList,name="list-tasks"),
    path("<str:pk>/task/",views.Details,name="task"),
    path("create/",views.createTask,name="create-task"),
    path("<str:pk>/update/",views.updateTask,name="update-task"),
    path("<str:pk>/delete/",views.deleteTask,name="delete-task"),

]