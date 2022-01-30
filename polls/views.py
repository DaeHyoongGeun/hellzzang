from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello가 아니라 world. You're at the polls index.")
