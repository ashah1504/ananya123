from django.db import models

# Create your models here.
class SpecialSkills(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length = 100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Special Skills"

class Project(models.Model):
    name = models.CharField(max_length= 100)
    techStack = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " " + self.link
    
    class Meta:
        verbose_name_plural = "Project"

class ContactUs(models.Model):
    name = models.CharField(max_length= 100)
    phone = models.CharField(max_length= 20)
    context = models.CharField(max_length= 100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
    
class WorkExp(models.Model):
    cmpName = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    shortDescription = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.cmpName + " " + self.position
    
    class Meta:
        verbose_name_plural = "Work Experience"
    
class Education(models.Model):
    EdChoices = [
        ('JR', "Junior"),
        ('SR', "Senior"),
        ('GR', "Graduate"),
    ]
    schName = models.CharField(max_length=50, null=True, blank=True)
    hist = models.CharField(choices=EdChoices, null=True, blank=True, max_length=10, default="Junior")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.schName + " " + self.hist
    
    class Meta:
        verbose_name_plural = "Education"