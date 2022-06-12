from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    m_frist_name = models.CharField(max_length=100)
    m_last_name = models.CharField(max_length=100)
    m_email = models.EmailField(primary_key=True)
    m_password = models.CharField(max_length=100)

    class Meta:
        db_table = "user"
    
    def __str__(self):
        return self.m_frist_name

class Home(models.Model):
    m_title = models.CharField(max_length=100)
    m_date_and_time = models.DateTimeField(default=datetime.now,blank=True)
    m_summary = models.TextField(default='')
    m_categories = models.CharField(max_length=100)

    class Meta:
        db_table = "blog"
    
    def __str__(self):
        return self.m_title        

