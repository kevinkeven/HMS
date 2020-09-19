from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
import uuid

# Create your models here.
class Patient(models.Model):
    MALE = 1
    FEMALE = -1
    OTHER = 0
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='patients/%y/%m/%d', blank=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    slug = models.SlugField(max_length=180, db_index=True)
    address = models.CharField(max_length=90)
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=90)
    phone = models.CharField(max_length=16)
    email = models.EmailField(blank=True)
    gender = models.SmallIntegerField(choices=GENDER)
    added = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('patient:patient_info',
                        args=[
                            self.id,
                            self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + " " + self.last_name)
        super(Patient, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'))

class Condition(models.Model):
    O = 1
    A = 2
    AB = 3
    B = 4
    B_TYPES = (
        (O, 'O'),
        (A, 'A'),
        (AB, 'AB'),
        (B, 'A'),
    )
    owner = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_type = models.SmallIntegerField(choices=B_TYPES)

    def __str__(self):
        return '{}'.format(self.owner)