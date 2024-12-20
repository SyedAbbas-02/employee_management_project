from django.utils import timezone

from employees import models

class Employee(models.Model):
    # ... other fields ...
    created_date = models.DateTimeField(auto_now_add=True)
    # ... other fields ... 