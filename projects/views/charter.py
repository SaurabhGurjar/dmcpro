from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)

from projects.forms import ProjectCharterForm
from projects.models import Project, ProjectCharter


# ==================================================
# CHARTER DETAIL
# ==================================================

class CharterDetailView(LoginRequiredMixin, DetailView):
    model = ProjectCharter
    template_name = "projects/charter/charter_detail.html"
    context_object_name = "charter"

    def get_object(self):
        self.project = get_object_or_404(
            Project,
            pk=self.kwargs["project_pk"],
            created_by=self.request.user,
        )

        return ProjectCharter.objects.filter(
            project=self.project
        ).first()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj is None:
            return redirect(
                "projects:charter-create",
                project_pk=self.kwargs["project_pk"],
            )

        self.object = obj

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["project"] = self.project
        context["active_tab"] = "charter"

        return context


# ==================================================
# CHARTER CREATE
# ==================================================

class CharterCreateView(LoginRequiredMixin, CreateView):
    model = ProjectCharter
    form_class = ProjectCharterForm
    template_name = "projects/charter/charter_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(
            Project,
            pk=self.kwargs["project_pk"],
            created_by=request.user,
        )

        # Prevent duplicate charter
        if ProjectCharter.objects.filter(
            project=self.project
        ).exists():
            return redirect(
                "projects:charter-detail",
                project_pk=self.project.pk,
            )

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.project = self.project
        self.object.save()

        messages.success(
            self.request,
            "Project charter created successfully.",
        )

        return redirect(
            "projects:charter-detail",
            project_pk=self.project.pk,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["project"] = self.project
        context["active_tab"] = "charter"

        return context


# ==================================================
# CHARTER UPDATE
# ==================================================

class CharterUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectCharter
    form_class = ProjectCharterForm
    template_name = "projects/charter/charter_form.html"

    def get_object(self, queryset=None):
        self.project = get_object_or_404(
            Project,
            pk=self.kwargs["project_pk"],
            created_by=self.request.user,
        )

        return get_object_or_404(
            ProjectCharter,
            project=self.project,
        )

    def form_valid(self, form):
        self.object = form.save()

        messages.success(
            self.request,
            "Project charter updated successfully.",
        )

        return redirect(
            "projects:charter-detail",
            project_pk=self.project.pk,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["project"] = self.project
        context["active_tab"] = "charter"

        return context