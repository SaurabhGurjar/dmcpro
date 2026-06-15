from django.contrib import admin

from .models import Project, ProjectTeamMember


class ProjectTeamMemberInline(admin.TabularInline):
    model = ProjectTeamMember
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "project_code",
        "title",
        "project_type",
        "priority",
        "status",
        "created_by",
        "start_date",
        "target_completion_date",
    )

    list_filter = (
        "project_type",
        "priority",
        "status",
    )

    search_fields = (
        "project_code",
        "title",
        "problem_statement",
        "goal_statement",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        ProjectTeamMemberInline,
    ]


@admin.register(ProjectTeamMember)
class ProjectTeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "employee_name",
        "role",
        "project",
        "department",
    )

    list_filter = (
        "role",
    )

    search_fields = (
        "employee_name",
        "employee_id",
    )