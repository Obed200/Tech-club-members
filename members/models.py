from django.db import models

class Member(models.Model):
    # image = models.ImageField()
    # chatgpt suggestions for image
    profile_image = models.ImageField(upload_to='productionfiles/', blank=True, null=True)

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="",null=False)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    # comment of django image
    
# class MemberImage(models.Model):
#     member = models.ForeignKey(
#         Member, on_delete=models.CASCADE, related_name="images"
#     )
#     image = models.ImageField(upload_to="members/")
#     is_main = models.BooleanField(default=False)

#     def __str__(self):
#         return self.member.name


