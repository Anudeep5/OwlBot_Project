from django.urls import path  # type: ignore
from . import views
from .views import ScheduleTaskView

app_name = "chatbot"

urlpatterns = [
    # Chatbot Query API
    path("query/", views.chatbot_query, name="chatbot_query"),
    # Admin Login API
    path("admin/login/", views.admin_login, name="admin_login"),
    # Admin Logout API
    path("admin/logout/", views.admin_logout, name="admin_logout"),

    path(
        "schedule/", 
        ScheduleTaskView.as_view(), 
        name="schedule_task"
    ),
]
