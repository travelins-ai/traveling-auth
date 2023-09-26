from django.template import loader
from django.http import HttpResponse

from decouple import config
HOST_CURRENT_APP = config('HOST_CURRENT_APP', default='http://localhost:8000')
SITE_URL= config('HOST_CLIENT', default='http://localhost:3000')
# Create your views here.
def index(request): 
    template = loader.get_template("google.html")
    context = {
        "redirect_uri": HOST_CURRENT_APP,
        "success_redirect_uri": SITE_URL,
    }
    return HttpResponse(template.render(context, request))