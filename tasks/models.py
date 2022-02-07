from django.db import models
from django.contrib.auth.models import User

class task(models.Model):
    PENDING='1'
    ONGOING='2'
    FINISHED='3'


    STATUS_CHOICES=[
        (PENDING,'pending'),
        (ONGOING,'ongoing'),
        (FINISHED,'finished'),
    ]
    #--------ACTUAL FIELDS------------------
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    content=models.TextField()
    status=models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDING,
        )
    author=models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE)


    #allows to show the title on the admin site
    def __str__(self):
        return self.title
    #custom dethod to show a preview on the template
    def preview(self):
        return self.content[:50]+'...'
