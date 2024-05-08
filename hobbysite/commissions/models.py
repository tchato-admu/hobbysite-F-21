from django.db import models
from django.urls import reverse
from user_management.models import Profile


class Commission(models.Model):
    status_choices = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued')
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="commission")
    
    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse("commissions:commissions_detail", args=[str(self.pk)])


class Job(models.Model):
    status_choices = [
        ('Open', 'Open'),
        ('Full', 'Full')
    ]
    
    commission = models.ForeignKey(
        Commission, 
        on_delete=models.CASCADE, 
        related_name="job")
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=status_choices, default='Open')
    
    class Meta:
        ordering = ['-status', '-manpower_required', 'role']


    def __str__(self):
        return str(self.role)


class JobApplication(models.Model):
    status_choices = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_application")
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-status', '-applied_on']