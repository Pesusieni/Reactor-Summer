from django.db import models
from django.forms import ModelForm , CharField
# Create your models here.

class Tag(models.Model):
    name = models.CharField(unique=True,max_length=20)
    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(null=True,blank=True)
    tags_list = models.ManyToManyField(Tag,blank=True)
    uploader = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    image = models.ImageField(upload_to='photos/')


    def __str__(self):
        return self.title
class Reply(models.Model):
    nick_name = models.CharField(max_length=20)
    reply = models.TextField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photo)
class PhotoForm(ModelForm):
    tags_list = CharField(required=False,max_length=255)
    class Meta:
        model = Photo
        fields = ['title','description','uploader','image']
    def clean_tags(self):
        data = self.cleaned_data['tags_list']
        data = data.spli[',']
    def clean_tag_list(self):
        data = self.cleaned_data
        tags_list = data.get('tags_list', None)
        if tags_list is not None:
            for tag_name in tags_list.split(','):
                try:
                    tag = Tag.objects.get(name=tag_name)
                except Tag.DoesNotExist:
                    Tag(name=tag_name).save()
        return tags_list
