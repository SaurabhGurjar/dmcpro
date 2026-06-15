from django.db import models

from .project import Project


class ProjectCharter(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="charter",
    )

    # ==========================
    # Business Information
    # ==========================

    business_case = models.TextField(blank=True)

    problem_statement = models.TextField(blank=True)

    goal_statement = models.TextField(blank=True)

    # ==========================
    # Scope
    # ==========================

    scope_in = models.TextField(blank=True)

    scope_out = models.TextField(blank=True)

    benefits = models.TextField(
        blank=True,
        help_text="Expected business benefits from this project.",
    )

    # ==========================
    # Planning
    # ==========================

    assumptions = models.TextField(blank=True)

    constraints = models.TextField(blank=True)

    success_metrics = models.TextField(blank=True)

    financial_impact = models.TextField(blank=True)

    # ==========================
    # Approval
    # ==========================

    approved_by = models.CharField(
        max_length=100,
        blank=True,
    )

    approval_date = models.DateField(
        null=True,
        blank=True,
    )

    # ==========================
    # Additional Notes
    # ==========================

    notes = models.TextField(blank=True)

    # ==========================
    # Audit Fields
    # ==========================

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["project"]

    def __str__(self):
        return f"Charter - {self.project.project_code}"