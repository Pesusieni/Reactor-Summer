from django.shortcuts import render
from photo.models import Tag , Photo , Reply ,PhotoForm
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseForbidden
from django.template import RequestContext, loader


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
def picture(request,picture_id):
    reply_list = Photo.reply_set.all()
    reply_list = reply_list.order_by('-timestamp')[:100]

    pass
def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            form.clean_tag_list()
            # Create a new Server object.
            form.save()
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
