from django.shortcuts import render
from photo.models import Tag , Author , Photo
def frontpage(request):
    try:
        picture = Photo.objects.order_by('?').first()
        template = loader.get_template('front.html')
        context = RequestContext(request, {
            'picture' : picture,
        })
        return HttpResponse(template.render(context))

    except:
        try:

        except:
            raise Http404
def picture(request,picture_id):
    pass
