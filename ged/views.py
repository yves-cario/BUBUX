from django.http import HttpResponse

def index(request):
    return HttpResponse("Where is your god now ?")
