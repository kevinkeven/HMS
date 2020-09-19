from django import forms
from .models import Patient, Condition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Submit
from crispy_forms.bootstrap import InlineRadios, InlineField

class ConditionForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        widget = forms.HiddenInput,
        queryset = Patient.objects.all(),
        disabled = True,
        required = False,
    )
    blood_type = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = Condition.B_TYPES,
    )

    def __init__(self, *args, **kwargs):
        super(ConditionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            InlineRadios('blood_type'),
            Submit('submit', 'Save', css_class='btn btn-block btn-dark')
            
        )
    
    class Meta:
        model = Condition
        fields = ('owner', 'blood_type',)
class PatientUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            'address',
             'street_address',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-6 mb-0'),
            ),
            'phone',
            'email',
            Submit('submit', 'Save', css_class='btn btn-block btn-primary')
        )
    
    class Meta:
        model = Patient
        fields = ('address', 'street_address', 'city', 'state', 'phone', 'email')
class PatientForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Gender',
        widget=forms.RadioSelect,
        choices=Patient.GENDER,
    )
    slug = forms.SlugField(
        widget = forms.HiddenInput,
        disabled = True,
        required=False,
    )
    image = forms.FileField(
        widget=forms.FileInput,
        required=False,
        label='Patient Image',
    )
    
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            'image',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('street_address', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('city', css_class='form-group col-md-4 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),
            ),
            'email',
            InlineRadios('gender'),
            Submit('submit', 'Save', css_class='btn btn-block btn-primary')
        )

    
    class Meta:
        model = Patient
        fields = ('slug', 'image', 'first_name', 'last_name', 'address', 'street_address', 'city', 'state', 'phone', 'email', 'gender')