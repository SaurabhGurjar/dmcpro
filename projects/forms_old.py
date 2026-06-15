from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        exclude = (
            "created_by",
            "created_at",
            "updated_at",
        )

        widgets = {
            "problem_statement": forms.Textarea(attrs={"rows": 4}),
            "goal_statement": forms.Textarea(attrs={"rows": 4}),
            "business_case": forms.Textarea(attrs={"rows": 4}),
            "scope_in": forms.Textarea(attrs={"rows": 3}),
            "scope_out": forms.Textarea(attrs={"rows": 3}),
            "benefits": forms.Textarea(attrs={"rows": 3}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "target_completion_date": forms.DateInput(attrs={"type": "date"}),
            "actual_completion_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            css = "form-control"

            if isinstance(field.widget, forms.Select):
                css = "form-select"

            field.widget.attrs["class"] = css