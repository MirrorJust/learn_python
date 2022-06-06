from django.db import models


# id - int
# name_skill - text
# created_at- DateTime
# update_at - DateTime
# photo - Image
class Skill(models.Model):
    name_skill = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name_skill
