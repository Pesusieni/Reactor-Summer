from django.shortcuts import render
from photo.models import Tag , Photo , Reply ,PhotoForm,ReplyForm
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseForbidden,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse


def index(request):
    picture = Photo.objects.order_by('?').first()
    return render(request,'photo/index.html',{'picture':picture})
def photo(request,picture_id):
    try:
        photo = Photo.objects.get(pk = picture_id)
    except:
        raise Http404
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            temp = form.save(commit = False)
            temp.photo_id = picture_id
            temp.save()

    reply_list = photo.reply_set.all()
    reply_list = reply_list.order_by('-timestamp')[:100]
    replyform = ReplyForm()
    return render(request,'photo/photo.html',{
    'photo' : photo,
    'replyform' : replyform,
    'reply_list' : reply_list
    })
def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            tempdata = form.clean_tag_list()
            temp = form.save(commit=False)
            temp.save()
            for item in tempdata:
                temp.tags.add(item)
            form.save_m2m()
            return HttpResponseRedirect(reverse(photo, args=[temp.pk]))
        else:
            return render(request,'photo/upload.html',{'form': form})
    form = PhotoForm()
    return render(request,'photo/upload.html',{'form': form})

def about(request):
    return render(request,'photo/about.html')
def specific_search(request,photo_tag):
    photos = Photo.objects.filter(tags__name=photo_tag)
    photos = photos.order_by('timestamp')[:50]
    return render(request,'photo/photos.html',{'photos' : photos})
def search(request):
    if request.method == "POST":
        data = request.POST['tags'].lower()
        if len(data)==0:
            photos = Photo.objects.order_by('?')[:50]
            return render(request,'photo/photos.html',{'photos' : photos})
        photos = Photo.objects
        for item in data.split(','):
            photos = photos.filter(tags__name=item)
        photos = photos.order_by('timestamp')[:50]
        return render(request,'photo/photos.html',{'photos' : photos})
    return render(request,'photo/search.html')
