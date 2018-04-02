from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from patients.models import PatientsInfo
# Create your models here.

class Item(models.Model):
    #assosiateions
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    patient = models.ForeignKey(PatientsInfo)

    #item stuff
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, null=True, blank=True, default='Male', help_text='Male/Female')
    ethnicity = models.CharField(max_length=10, null=True, blank=True, default='Chinese', help_text='Chinese/Malay/Indian/Eurasian/Others')
    smoker=models.CharField(max_length=3, blank=True, default='No', help_text='Yes/No')

    initial_visit = models.CharField(max_length=6, blank=True, help_text='AM/PM/Night')
    fever = models.CharField(max_length=5, blank=True, help_text='Yes/No')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('diseases:detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-updated','-timestamp']

    def get_initialvisit(self):
        return self.initial_visit.split(",")

    def get_fever(self):
        return self.fever.split(",")

