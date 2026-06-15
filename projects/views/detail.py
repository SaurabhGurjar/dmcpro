from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from projects.models import Project
from projects.models.enums import TeamRole


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

    def get_queryset(self):
        return Project.objects.filter(
            created_by=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["active_tab"] = "overview"

        project = self.object

        team_members = project.team_members.all()

        context["leader"] = team_members.filter(
            role=TeamRole.LEADER
        ).first()

        context["sponsor"] = team_members.filter(
            role=TeamRole.SPONSOR
        ).first()

        context["facilitator"] = team_members.filter(
            role=TeamRole.FACILITATOR
        ).first()

        context["members"] = team_members.filter(
            role=TeamRole.TEAM_MEMBER
        )

        return context