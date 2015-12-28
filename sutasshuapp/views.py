from django.shortcuts import render, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import UploadForm
from .models import Image

def index(request):
    images = Image.objects.all()
    return render_to_response(
        'index.html',
        {'images': images},
        context_instance=RequestContext(request)
    )


def add(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newimage = Image(image=request.FILES['imagefile'])
            newimage.save()

            return HttpResponseRedirect(reverse('sutasshuapp.views.index'))
    else:
        form = UploadForm()

    return render_to_response(
        'add.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
