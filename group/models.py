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

class Skillset(BaseModel):
    id = models.ForeignKey(User, on_delete=models.CASCADE,default=00)
    coding = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    leadership = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    communication = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    presentation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        return self.id