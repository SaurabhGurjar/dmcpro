from django.conf import settings
from django.db import models

from .enums import (
    ProjectPriority,
    ProjectStatus,
    ProjectType,
)


class Project(models.Model):
    title = models.CharField(max_length=200)

    project_code = models.CharField(
        max_length=50,
        unique=True,
    )

    project_type = models.CharField(
        max_length=20,
        choices=ProjectType.choices,
        default=ProjectType.SIX_SIGMA,
    )

    priority = models.CharField(
        max_length=10,
        choices=ProjectPriority.choices,
        default=ProjectPriority.MEDIUM,
    )

    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.DEFINE,
    )

    problem_statement = models.TextField()

    goal_statement = models.TextField()

    business_case = models.TextField(
        blank=True,
        default="",
    )

    scope_in = models.TextField(
        verbose_name="Scope (In)",
        blank=True,
        default="",
    )

    scope_out = models.TextField(
        verbose_name="Scope (Out)",
        blank=True,
        default="",
    )

    benefits = models.TextField(
        blank=True,
        default="",
    )

    start_date = models.DateField()

    target_completion_date = models.DateField()

    actual_completion_date = models.DateField(
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.project_code} - {self.title}"