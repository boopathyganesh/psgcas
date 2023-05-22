from django import forms

from django import forms

class Reg_form(forms.Form):
    rollno = forms.CharField(
        label='Reg.No',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Reg-No (Block Letters)'}),
    )
    full_name = forms.CharField(
        label='Full Name (as per given in admission)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name with Initial'}),
    )
    department = forms.CharField(
        label='Department',
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
    )
    current_pursuing = forms.ChoiceField(
        label='Present Graduation Status',
        choices=(
            ('Under Graduation', 'Under Graduation'),
            ('Post Graduation', 'Post Graduation'),
        ),
        widget=forms.RadioSelect,
    )
    con = forms.IntegerField(
        label='Contact No',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Eg. Only WhatsApp number'}),
    )
    altcon = forms.CharField(
        label='Alternative Contact No',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg. Only WhatsApp number'}),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Official Mail'}),
    )
    aemail = forms.EmailField(
        label='Alternative Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Secondary Mail'}),
    )
    dob = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(attrs={'class': 'form-control'}),
    )
    age = forms.IntegerField(
        label='Age',
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
    )
    gender = forms.ChoiceField(
        label='Gender',
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
        ),
        widget=forms.RadioSelect,
    )
    marital_sts = forms.ChoiceField(
        label='Marital Status',
        choices=(
            ('Married', 'Married'),
            ('Unmarried', 'Unmarried'),
        ),
        widget=forms.RadioSelect,
    )

    def clean_rollno(self):
        rollno = self.cleaned_data['rollno']
        # Add custom validation logic for rollno if needed
        return rollno

    # Add clean methods for other fields if needed


