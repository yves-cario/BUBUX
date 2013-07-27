from django.shortcuts import render

from ged.models import Document

def index(request):
    documents = Document.objects.all()
    context = {'documents': documents}

    return render(request, 'ged/index.html', context)
