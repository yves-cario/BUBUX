from django.http import HttpResponse
from django.template import RequestContext, loader

from ged.models import Document

def index(request):
    documents = Document.objects.all()
    template = loader.get_template('ged/index.html')
    context = RequestContext(request, {
        'documents': documents
    })

    return HttpResponse(template.render(context))
