from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
import datetime as dt



        
class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    bio = models.TextField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
            if created:
                    Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
                instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    
    @classmethod
    def search_user(cls, name):
        userprof = Profile.objects.filter(user__username__icontains = name)
        return userprof
# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    # image_caption = models.TextField(max_length =40)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name='Image_likes')
    # profile = models.ForeignKey(Profile, null = True,related_name='image')
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    comment = models.ForeignKey
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # likes = models.PositiveIntegerField(default=0)

    def save_image(self):
        self.save()
    
    @classmethod
    def get_images(cls, profile):
        image = Image.objects.filter(id)
        return image
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(id)
        return images

    @classmethod
    def get_image_id(cls, id):
        identity = Image.objects.get(id)
        return identity

    # def get_like_url(self):
    #     reverse=("images:like-toggle", kwargs={"slug": self.slug})
    #     return reverse


class Comment(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,null = True)
    image = models.ForeignKey(Image,related_name='comment')
    


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


    @classmethod
    def get_commentimage(cls,id):
        comments = Comments.objects.filter(image__pk = id)
        
        return comments
