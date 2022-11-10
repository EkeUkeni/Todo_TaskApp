from django.urls import path
from taskapp import views

app_name = "taskapp"

urlpatterns = [
    path("", views.index, name="home"),
    path("create-task/", views.create_task, name="task-create"),
    path("update-task/<str:pk>/", views.update_task, name="task-update"),
    path("delete-task/<str:pk>/", views.delete_task, name="task-delete")
]