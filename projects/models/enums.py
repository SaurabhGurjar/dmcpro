from django.db import models


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