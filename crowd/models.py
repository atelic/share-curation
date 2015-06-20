from django.db import models
from sharepa import ShareSearch
import json

# Create your models here.
class UserName(models.Model):
  pass  

class Password(models.Model):
  pass  

class Data(models.Model):
  def index():
    search = ShareSearch()
    first_ten = search.execute()
    return json.loads(first_ten)
    
