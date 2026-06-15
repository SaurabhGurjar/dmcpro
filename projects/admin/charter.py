from django.contrib import admin

from projects.models import ProjectCharter


@admin.register(ProjectCharter)
class ProjectCharterAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "approved_by",
        "approval_date",
    )