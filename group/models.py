from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import random
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True

class FormDetail(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    status = models.BooleanField(default=False)  # Consider using a more descriptive name for the status field
    def __str__(self):
        return self.title

class Skillset(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    form_detail = models.ForeignKey(FormDetail,related_name='formdetail', on_delete=models.CASCADE)  # Link to FormDetail
    coding = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    leadership = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    communication = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    presentation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.form_detail
    

class detail(BaseModel):
    press = models.CharField(default = 'Unknown', max_length=50)
