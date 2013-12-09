from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from note.models import Autor, Stat
from django.core.urlresolvers import reverse
from django.views import generic

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext

class IndexView(generic.ListView):
    template_name = 'note/index.html'
    context_object_name = 'latest_stat_list'
    model = Stat
    paginate_by = 3
    
class DetailView(generic.DetailView):
    model = Stat
    template_name = 'note/detail.html'

class AutorView(generic.DetailView):
    model = Autor
    template_name = 'note/autor.html'
