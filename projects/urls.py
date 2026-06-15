from django.urls import path

from .views.delete import ProjectDeleteView
from .views import ProjectListView, ProjectCreateView, ProjectDetailView, TeamListView, ProjectCreateView, TeamCreateView, TeamUpdateView, TeamDeleteView
from .views.update import ProjectUpdateView
from .views.team import *

app_name = "projects"

urlpatterns = [
    path(
        "",
        ProjectListView.as_view(),
        name="project-list",
    ),

    path(
        "create/",
        ProjectCreateView.as_view(),
        name="project-create",
    ),

    path(
        "<int:pk>/",
        ProjectDetailView.as_view(),
        name="project-detail",
    ),

    path(
        "<int:pk>/edit/",
        ProjectUpdateView.as_view(),
        name="project-update",
    ),

    path(
    "<int:pk>/delete/",
    ProjectDeleteView.as_view(),
    name="project-delete",
    ),
    
    # Team Management
    path(
        "<int:project_pk>/team/",
        TeamListView.as_view(),
        name="team-list",
    ),

    path(
        "<int:project_pk>/team/add/",
        TeamCreateView.as_view(),
        name="team-create",
    ),

    path(
        "team/<int:pk>/edit/",
        TeamUpdateView.as_view(),
        name="team-update",
    ),

    path(
        "team/<int:pk>/delete/",
        TeamDeleteView.as_view(),
        name="team-delete",
    ),
]