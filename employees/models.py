from django.db import models
from django.utils import timezone

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Sales', 'Sales'),
    ]
    
    COURSE_CHOICES = [
        ('MCA', 'MCA'),
        ('BCA', 'BCA'),
        ('BSC', 'BSC'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    course = models.CharField(max_length=5, choices=COURSE_CHOICES)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # For handling unique email during updates
        if self.pk:  # If this is an update
            orig = Employee.objects.get(pk=self.pk)
            if orig.email != self.email:  # Only check if email changed
                if Employee.objects.filter(email=self.email).exists():
                    raise ValueError('Email already exists')
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']