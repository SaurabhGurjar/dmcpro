from django import forms
from projects.models import ProjectTeamMember


class TeamMemberForm(forms.ModelForm):

    class Meta:
        model = ProjectTeamMember
        exclude = ("project",)

        widgets = {
            "employee_name": forms.TextInput(attrs={"class": "form-control"}),
            "employee_id": forms.TextInput(attrs={"class": "form-control"}),
            "designation": forms.TextInput(attrs={"class": "form-control"}),
            "department": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-select"}),
            "display_order": forms.NumberInput(attrs={"class": "form-control"}),
        }