from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    title = models.CharField(max_length=255)
    work_description = models.TextField()
    pincode = models.CharField(max_length=6)
    task_type = models.CharField(max_length=50, choices=[
        ('grocery', 'Grocery'),
        ('tutoring', 'Tutoring'),
        ('delivery', 'Delivery'),
    ])
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')  # New status field (pending, accepted, declined)

    def __str__(self):
        return self.title

