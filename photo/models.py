from django.db import models
from django.forms import ModelForm , CharField

class Tag(models.Model):
    name = models.CharField(unique=True,max_length=20)
    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(null=True,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
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
class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['nick_name','reply']

class PhotoForm(ModelForm):
    tags_list = CharField(required=False,max_length=255)
    class Meta:
        model = Photo
        fields = ['title','description','uploader','image']
    def clean_tag_list(self):
        data = self.cleaned_data
        tags_list = data.get('tags_list', None)
        temp = []
        if tags_list is not None:
            tags_list = tags_list.lower()
            for tag_name in tags_list.split(','):
                try:
                    tag = Tag.objects.get(name=tag_name)
                    temp.append(tag)
                except Tag.DoesNotExist:
                    tag = Tag.objects.create(name=tag_name)
                    print(tag)
                    temp.append(tag)

        return temp
