from django.views.generic import View, TemplateView
from django.http import HttpResponse

class IndexView(TemplateView):

	template_name = "index.html"