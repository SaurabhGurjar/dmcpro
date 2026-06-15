from django.contrib import admin
from projects.models import ProjectTeamMember


@admin.register(ProjectTeamMember)
class ProjectTeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "employee_name",
        "project",
        "role",
        "department",
    )

    list_filter = (
        "role",
        "project",
    )

    search_fields = (
        "employee_name",
        "employee_id",
        "email",
    )