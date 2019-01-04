from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from flowback.models import Well_Profile
from flowback.utils.choices import well_choice_gen
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions




class CrispyModelForm(forms.ModelForm):
    class Meta:
        model = Well_Profile
        fields = '__all__'
        widgets = {
            'company': forms.TextInput(attrs={'placeholder': 'Please select company name', 'required': True}),
            'well_name': forms.TextInput(attrs={'placeholder': 'Please Enter Well Name', 'required': True}),    
        }

    def __init__(self, *args, **kwargs):
        super(CrispyModelForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('Submit', 'Submit'))
