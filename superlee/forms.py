from django import forms

class RegistrationForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]
    PURSUING_CHOICES = [
        ('Under Graduation', 'Under Graduation'),
        ('Post Graduation', 'Post Graduation'),
    ]
    rollno = forms.CharField(max_length=100, label='Reg.No', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Reg-No'}))
    full_name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name with Initial'}))
    current_pursuing = forms.ChoiceField(choices=PURSUING_CHOICES, label='Pursuing Graduation', widget=forms.RadioSelect(attrs={'class': 'form-check-input','type':'radio'}))
    dept = forms.CharField(max_length=100, label='Department', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg. Master of Computer Applications'}))
    con = forms.CharField(max_length=100, label='Contact No', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg. Only whatsapp number'}))
    altcon = forms.CharField(max_length=100, label='Alternative Contact No', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg. Only whatsapp number'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Official Mail'}))
    aemail = forms.EmailField(label='Alternative Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Secondary Mail'}))
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='Age', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg.21'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', widget=forms.RadioSelect(attrs={'class':'radio form-check-input'}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Marital Status', widget=forms.RadioSelect(attrs={'class': 'radio form-check-input'}))

