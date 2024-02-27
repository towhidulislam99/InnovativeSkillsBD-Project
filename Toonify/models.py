from django.db import models

# Create your models here.

class Sliderpage(models.Model):
    slider_heading = models.CharField(max_length = 500)
    slider_paragraph = models.CharField(max_length = 200)
    slider_photo = models.ImageField(upload_to='Slider Photo/', default='No images')
    
    
class WorkProcedureHeading(models.Model):
    work_pro_heading = models.CharField(max_length = 500)
    

class WorkProcedureTopic(models.Model):
    work_pro_paragraph = models.CharField(max_length = 500)
    

class ToonificationHeading(models.Model):
   toonification_heading = models.CharField(max_length = 500)
   
class ToonificationImage(models.Model):
   toonification_photo = models.ImageField(upload_to='ToonificationImage/', default='No images')
   

class HyperparametersHeading(models.Model):
   hyperparameters_heading = models.CharField(max_length = 500)
   
class HyperparametersImage(models.Model):
   hyperparameters_photo = models.ImageField(upload_to='HyperparametersImage/', default='No images')