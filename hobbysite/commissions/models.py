from django.db import models
from django.urls import reverse


class Commissions(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("commissions:commissions_detail", args=[str(self.pk)])


    class Meta:
        ordering = ["created_on"]

    
    
class Comments(models.Model):
    commission = models.ForeignKey(
        to=Commissions, on_delete=models.CASCADE, related_name="comments"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_on"]