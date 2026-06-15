from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from projects.models import Project


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "projects/project_confirm_delete.html"
    success_url = reverse_lazy("projects:project-list")

    def get_queryset(self):
        return Project.objects.filter(
            created_by=self.request.user
        )

    def form_valid(self, form):
        messages.success(
            self.request,
            "Project deleted successfully."
        )
        return super().form_valid(form)