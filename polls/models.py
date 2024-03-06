from django.db import models
from django.utils.text import slugify

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100, default="Name")
    EmailAddress = models.EmailField()
    Subject = models.CharField(max_length=200, default=" Subject")  # Set your desired default subject
    message = models.TextField(max_length=2000)
    datetimes= models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.Name

STATUS = (
    (0,"Draft"), 
    (1,"Publish")
)     

class Blog(models.Model):
    image=models.ImageField(upload_to="media") 
    name=models.CharField(max_length=200) 
    datetimes= models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=10000) 
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now_add= True)
    slug=models.SlugField(null=True,blank=True,unique=True)
    

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)  
        