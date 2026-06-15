from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from projects.forms import TeamMemberForm
from projects.models import Project, ProjectTeamMember
from projects.models.enums import TeamRole


# ==================================================
# TEAM LIST
# ==================================================

class TeamListView(LoginRequiredMixin, ListView):
    model = ProjectTeamMember
    template_name = "projects/team/team_list.html"
    context_object_name = "members"

    def get_queryset(self):
        self.project = get_object_or_404(
            Project,
            pk=self.kwargs["project_pk"],
            created_by=self.request.user,
        )

        return self.project.team_members.all().order_by(
            "display_order",
            "employee_name",
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        members = context["members"]

        context["project"] = self.project

        context["leader"] = members.filter(
            role=TeamRole.LEADER
        ).first()

        context["sponsor"] = members.filter(
            role=TeamRole.SPONSOR
        ).first()

        context["facilitator"] = members.filter(
            role=TeamRole.FACILITATOR
        ).first()

        context["team_members"] = members

        return context


# ==================================================
# TEAM CREATE
# ==================================================

class TeamCreateView(LoginRequiredMixin, CreateView):
    model = ProjectTeamMember
    form_class = TeamMemberForm
    template_name = "projects/team/team_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(
            Project,
            pk=self.kwargs["project_pk"],
            created_by=request.user,
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        member = form.save(commit=False)
        member.project = self.project

        if member.role in (
            TeamRole.LEADER,
            TeamRole.SPONSOR,
            TeamRole.FACILITATOR,
        ):
            exists = ProjectTeamMember.objects.filter(
                project=self.project,
                role=member.role,
            ).exists()

            if exists:
                form.add_error(
                    "role",
                    f"A {member.get_role_display()} already exists for this project.",
                )
                return self.form_invalid(form)

        member.save()
        self.object = member

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.project
        return context

    def get_success_url(self):
        return reverse(
            "projects:team-list",
            kwargs={
                "project_pk": self.project.pk,
            },
        )


# ==================================================
# TEAM UPDATE
# ==================================================

class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectTeamMember
    form_class = TeamMemberForm
    template_name = "projects/team/team_form.html"

    def get_queryset(self):
        return ProjectTeamMember.objects.filter(
            project__created_by=self.request.user,
        )

    def form_valid(self, form):
        member = form.save(commit=False)

        if member.role in (
            TeamRole.LEADER,
            TeamRole.SPONSOR,
            TeamRole.FACILITATOR,
        ):
            exists = ProjectTeamMember.objects.filter(
                project=member.project,
                role=member.role,
            ).exclude(
                pk=member.pk,
            ).exists()

            if exists:
                form.add_error(
                    "role",
                    f"A {member.get_role_display()} already exists for this project.",
                )
                return self.form_invalid(form)

        member.save()
        self.object = member

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.object.project
        return context

    def get_success_url(self):
        return reverse(
            "projects:team-list",
            kwargs={
                "project_pk": self.object.project.pk,
            },
        )


# ==================================================
# TEAM DELETE
# ==================================================

class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectTeamMember
    template_name = "projects/team/team_confirm_delete.html"

    def get_queryset(self):
        return ProjectTeamMember.objects.filter(
            project__created_by=self.request.user,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.object.project
        return context

    def get_success_url(self):
        return reverse(
            "projects:team-list",
            kwargs={
                "project_pk": self.object.project.pk,
            },
        )