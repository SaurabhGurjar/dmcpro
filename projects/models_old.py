from django.conf import settings
from django.db import models


# =========================================================
# CHOICES
# =========================================================

class ProjectType(models.TextChoices):
    SIX_SIGMA = "SIX_SIGMA", "Six Sigma"
    LEAN = "LEAN", "Lean"
    KAIZEN = "KAIZEN", "Kaizen"
    CAPA = "CAPA", "CAPA"
    OTHER = "OTHER", "Other"


class ProjectPriority(models.TextChoices):
    LOW = "LOW", "Low"
    MEDIUM = "MEDIUM", "Medium"
    HIGH = "HIGH", "High"
    CRITICAL = "CRITICAL", "Critical"


class ProjectStatus(models.TextChoices):
    DEFINE = "DEFINE", "Define"
    MEASURE = "MEASURE", "Measure"
    ANALYZE = "ANALYZE", "Analyze"
    IMPROVE = "IMPROVE", "Improve"
    CONTROL = "CONTROL", "Control"
    COMPLETED = "COMPLETED", "Completed"
    ON_HOLD = "ON_HOLD", "On Hold"
    CANCELLED = "CANCELLED", "Cancelled"


class TeamRole(models.TextChoices):
    LEADER = "LEADER", "Leader"
    SPONSOR = "SPONSOR", "Sponsor"
    FACILITATOR = "FACILITATOR", "Facilitator"
    TEAM_MEMBER = "TEAM_MEMBER", "Team Member"


# =========================================================
# PROJECT MODEL (MIGRATION SAFE VERSION)
# =========================================================

class Project(models.Model):
    title = models.CharField(max_length=200)

    project_code = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
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

    # -------------------------
    # Text fields (safe defaults)
    # -------------------------
    problem_statement = models.TextField(blank=True, default="")
    goal_statement = models.TextField(blank=True, default="")
    business_case = models.TextField(blank=True, default="")

    scope_in = models.TextField(blank=True, default="")
    scope_out = models.TextField(blank=True, default="")

    benefits = models.TextField(blank=True, default="")

    # -------------------------
    # Date fields (safe for old rows)
    # -------------------------
    start_date = models.DateField(null=True, blank=True)
    target_completion_date = models.DateField(null=True, blank=True)
    actual_completion_date = models.DateField(null=True, blank=True)

    # -------------------------
    # System fields
    # -------------------------
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.project_code or 'DRAFT'} - {self.title}"


# =========================================================
# TEAM MEMBER
# =========================================================

class ProjectTeamMember(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="team_members",
    )

    employee_name = models.CharField(max_length=100)

    employee_id = models.CharField(max_length=30, blank=True, default="")
    designation = models.CharField(max_length=100, blank=True, default="")

    role = models.CharField(
        max_length=20,
        choices=TeamRole.choices,
    )

    department = models.CharField(max_length=100, blank=True, default="")

    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=20, blank=True, default="")

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order", "employee_name"]
        verbose_name = "Project Team Member"
        verbose_name_plural = "Project Team Members"

    def __str__(self):
        return f"{self.employee_name} ({self.get_role_display()})"