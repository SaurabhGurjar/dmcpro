from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from projects.forms import ProjectForm
from projects.models import Project


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/project_form.html"

    def get_queryset(self):
        # Only allow users to edit their own projects
        return Project.objects.filter(created_by=self.request.user)

    def form_valid(self, form):
        messages.success(
            self.request,
            "Project updated successfully.",
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "projects:project-detail",
            kwargs={"pk": self.object.pk},
        )