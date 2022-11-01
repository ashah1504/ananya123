from pyexpat import model
from django.db.models.signals import post_save, post_delete
from .models import Project, SpecialSkills
from django.dispatch import receiver

@receiver(post_save, sender = Project) #@receiver is a decorator
def autoGenerateSpecialSkills(sender, instance, created, **kwargs):
    print("Signal Fire Automatic")
    if created:
        # print(instance)
        projectData = instance
        SpecialSkills.objects.create(
            name = projectData.name,
            description = projectData.description,
        )
        print("special skills created")

@receiver(post_delete, sender = Project)  
def autoSpecialSkillsGone(sender, instance, **kwargs):
    projectData = instance
    # print(projectData.name)
    # print(projectData.techStack)
    # print(projectData.description)
    # print(projectData.link)

    fetchdata = SpecialSkills.objects.get(name=projectData.name)
    fetchdata.delete()
    print("Post delete signal called")
    
 