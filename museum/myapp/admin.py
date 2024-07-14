from django.contrib import admin

# Register your models here.
from .models import Employee, Visitor, Artifact, Artist, Department, Booking, Feedback

admin.site.register(Employee)
admin.site.register(Visitor)
admin.site.register(Artifact)
admin.site.register(Artist)
admin.site.register(Department)
admin.site.register(Booking)
admin.site.register(Feedback)