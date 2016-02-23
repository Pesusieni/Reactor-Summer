from django.shortcuts import render
from photo.models import Tag , Photo , Reply ,PhotoForm
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

    reply_list = photo.reply_set.all()
    reply_list = reply_list.order_by('-timestamp')[:100]
    template = loader.get_template('photo/photo.html')
    context = RequestContext(request,{
    'photo' : photo
    })
    return HttpResponse(template.render(context))
def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            form.clean_tag_list()
            tempform = form.save(commit=False)
            tempform.save()
            form = form.save_m2m()
            print(tempform)
            return HttpResponseRedirect(reverse(photo, args=[tempform.pk]))
        else:
            print(form.errors)


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
