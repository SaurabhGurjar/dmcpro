from django.db import models
from django.db.models import Q
from django.utils import timezone

from .enums import TeamRole
from .project import Project


class ProjectTeamMember(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="team_members",
    )

    employee_name = models.CharField(
        max_length=100,
    )

    employee_id = models.CharField(
        max_length=30,
        blank=True,
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    role = models.CharField(
        max_length=20,
        choices=TeamRole.choices,
    )

    department = models.CharField(
        max_length=100,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    

    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = [
            "display_order",
            "employee_name",
        ]

        verbose_name = "Project Team Member"
        verbose_name_plural = "Project Team Members"

        constraints = [
            # Only one Leader per project
            models.UniqueConstraint(
                fields=["project", "role"],
                condition=Q(role="leader"),
                name="unique_leader_per_project",
            ),

            # Only one Sponsor per project
            models.UniqueConstraint(
                fields=["project", "role"],
                condition=Q(role="sponsor"),
                name="unique_sponsor_per_project",
            ),

            # Only one Facilitator per project
            models.UniqueConstraint(
                fields=["project", "role"],
                condition=Q(role="facilitator"),
                name="unique_facilitator_per_project",
            ),
        ]

    def __str__(self):
        return f"{self.employee_name} ({self.get_role_display()})"