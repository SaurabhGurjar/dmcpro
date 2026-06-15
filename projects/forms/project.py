from django import forms

from projects.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "title",
            "project_code",
            "project_type",
            "status",
            "priority",
            "start_date",
            "target_completion_date",
            "actual_completion_date",
        ]

        widgets = {
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