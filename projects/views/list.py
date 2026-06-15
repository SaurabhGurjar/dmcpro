from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from projects.models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return (
            Project.objects
            .filter(created_by=self.request.user)
            .order_by("-created_at")
        )