from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from note.models import Autor, Stat, Comment
from note.forms import CommentForm
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.forms.models import modelformset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
   

class IndexView(generic.ListView):
    template_name = 'note/index.html'
    context_object_name = 'latest_stat_list'
    queryset = Stat.objects.select_related('autor')
    paginate_by = 3
    

class AutorView(generic.DetailView):
    model = Autor
    template_name = 'note/autor.html'


class CommentView(generic.ListView):
    template_name = 'note/detail.html'
    context_object_name = 'latest_comment_list'
    queryset = Comment.objects.select_related('stat')


def article_detail(request, pk):
    article = get_object_or_404(Stat, pk=pk)
    
    form = CommentForm(data=request.POST or None)
    if form.is_valid():
        comment = form.save(commit = False)
        comment.stat = article
        comment.save()
        return redirect('note:detail', pk=pk)
    context = dict(form=form, stat=article)
    return render(request, 'note/detail.html', context)
