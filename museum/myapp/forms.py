from django import forms
from .models import Artist, Artifact, Employee, Visitor, Department, Booking, Feedback
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from django.core.validators import MinValueValidator

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['first_name', 'last_name','username', 'nationality', 'address', 'email', 'password', 'phone']
        widgets = {
            'password': forms.PasswordInput(),
        }

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now,
        validators=[MinValueValidator(timezone.now().date())]
    )

    class Meta:
        model = Booking
        fields = ['visitor_name', 'phone_number', 'amount', 'ticket_type', 'quantity', 'date', 'email']

class VisitorLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name',  'incharge', 'opening_time', 'closing_time']
        widgets = {
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'department', 'date_of_birth', 'sex', 'designation', 'address', 'phone1', 'phone2']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'nationality', 'address', 'date_of_birth', 'phone', 'artifact']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),  # Adjust rows as needed
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})  # HTML5 date input
        }

class ArtifactForm(forms.ModelForm):
    class Meta:
        model = Artifact
        fields = ['name', 'description', 'incharge', 'department', 'cost']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),  # Adjust rows as needed
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['sender_name', 'sender_email', 'message']