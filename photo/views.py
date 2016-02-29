from django.shortcuts import render
from photo.models import Tag , Photo , Reply ,PhotoForm,ReplyForm
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseForbidden,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse


def index(request):
    #try:
    picture = Photo.objects.order_by('?').first()
    print(picture)

    template = loader.get_template('photo/index.html')
    context = RequestContext(request, {
        'picture' : picture,
    })
    return HttpResponse(template.render(context))

    #except:
    #    raise Http404
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
    template = loader.get_template('photo/photo.html')
    context = RequestContext(request,{
    'photo' : photo,
    'replyform' : replyform,
    'reply_list' : reply_list
    })
    return HttpResponse(template.render(context))
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
            print(form.errors)
            template = loader.get_template('photo/upload.html')
            context = RequestContext(request, {
                'form': form
            })
            return HttpResponse(template.render(context))

    else:
        form = PhotoForm()
    template = loader.get_template('photo/upload.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))


def about(request):

    template = loader.get_template('photo/about.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))
def specific_search(request,photo_tag):
    photos = Photo.objects.filter(tags__name=photo_tag)
    photos = photos.order_by('timestamp')[:50]
    template = loader.get_template('photo/photos.html')
    context = RequestContext(request, {
    'photos' : photos
    })
    return HttpResponse(template.render(context))
def search(request):
    if request.method == "POST":
        data = request.POST['tags'].lower()
        print(data)
        if len(data)==0:
            photos = Photo.objects.order_by('?')[:50]
            template = loader.get_template('photo/photos.html')
            context = RequestContext(request, {
            'photos' : photos
            })
            return HttpResponse(template.render(context))
        photos = Photo.objects
        for item in data.split(','):
            photos = photos.filter(tags__name=item)
        photos = photos.order_by('timestamp')[:50]
        template = loader.get_template('photo/photos.html')
        context = RequestContext(request, {
        'photos' : photos
        })
        return HttpResponse(template.render(context))
    template = loader.get_template('photo/search.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
