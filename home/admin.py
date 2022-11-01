from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ContactUs)
admin.site.register(models.Education)
admin.site.register(models.Project)
admin.site.register(models.SpecialSkills)
admin.site.register(models.WorkExp)

