from django import forms
from visitors.models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = "__all__"