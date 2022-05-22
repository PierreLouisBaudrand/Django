from django.forms.models import ModelForm
from .models import Student,Cursus,Presence
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "phone",
            "comments",
            "cursus",
        )

class PresenceForm(ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.order_by('last_name'))
    class Meta:
        model = Presence
        fields = (
            "reason",
            "isMissing",
            "date",
            "student",
        )

class CallofRollForm(forms.Form):
    date = forms.DateInput()
    choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
    )
