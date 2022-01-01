from django.urls import path

from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("candidates_list", views.candidates_list, name="candidates_list"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("", views.cin, name="cin"),
    path("create_candidate", views.createCandidate, name = "create_candidate"),
    path("update_candidate/<str:pk>", views.update_Candidate, name = "update_candidate"),
    path("delete/<int:pk>/", views.delete, name = "delete"),
    path("vote/<str:pknumber>", views.vote, name = "vote")
]
