from django import forms

from projects.models import ProjectCharter


class ProjectCharterForm(forms.ModelForm):

    class Meta:
        model = ProjectCharter

        exclude = (
            "project",
            "created_at",
            "updated_at",
        )

        widgets = {
            "business_case": forms.Textarea(attrs={"rows": 4}),
            "problem_statement": forms.Textarea(attrs={"rows": 4}),
            "goal_statement": forms.Textarea(attrs={"rows": 4}),
            "scope_in": forms.Textarea(attrs={"rows": 3}),
            "scope_out": forms.Textarea(attrs={"rows": 3}),
            "benefits": forms.Textarea(attrs={"rows": 4}),
            "assumptions": forms.Textarea(attrs={"rows": 3}),
            "constraints": forms.Textarea(attrs={"rows": 3}),
            "success_metrics": forms.Textarea(attrs={"rows": 3}),
            "financial_impact": forms.Textarea(attrs={"rows": 3}),
            "notes": forms.Textarea(attrs={"rows": 4}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "target_completion_date": forms.DateInput(attrs={"type": "date"}),
            "approval_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            css = "form-control"

            if isinstance(field.widget, forms.Select):
                css = "form-select"

            field.widget.attrs["class"] = css