from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
class Visitor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)  # Ensure this field is included
    address = models.TextField()  # Ensure this field is included
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Booking(models.Model):
    visitor_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, default='0000000000')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    date = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    email = models.EmailField(default='example@example.com' )  # Add this field

    def __str__(self):
        return f"{self.visitor_name} - {self.date}"

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    incharge = models.CharField(max_length=100)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10)
    designation = models.CharField(max_length=100)
    address = models.TextField()
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    address = models.TextField()  # Assuming address corresponds to "Address" in the form
    date_of_birth = models.DateField(null=True, blank=True)  # Assuming "Artifact" corresponds to date_of_birth
    phone = models.CharField(max_length=15)
    artifact=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Artifact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    incharge = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback from {self.sender_name} at {self.sent_at}"
