from django.db import models

from .project import Project


class ProjectCharter(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="charter",
    )

    business_case = models.TextField(blank=True)

    problem_statement = models.TextField(blank=True)

    goal_statement = models.TextField(blank=True)

    scope_in = models.TextField(blank=True)

    scope_out = models.TextField(blank=True)

    expected_benefits = models.TextField(blank=True)

    assumptions = models.TextField(blank=True)

    constraints = models.TextField(blank=True)

    success_metrics = models.TextField(blank=True)

    financial_impact = models.TextField(blank=True)

    start_date = models.DateField(
        null=True,
        blank=True,
    )

    target_completion_date = models.DateField(
        null=True,
        blank=True,
    )

    approved_by = models.CharField(
        max_length=100,
        blank=True,
    )

    approval_date = models.DateField(
        null=True,
        blank=True,
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Charter - {self.project.title}"