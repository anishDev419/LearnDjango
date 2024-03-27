from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from django.db.models import F
import logging

from members.models import Member


# Create your views here.
class Ex2View(TemplateView):
    template_name = "ex2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = "GET CONTEXT DATA"
        context['title'] = "ex2"
        return context


class PostPreLoadTaskView(RedirectView):
    pattern_name = "cbv:single-post"
    members = Member.objects.latest("id")

    def get_redirect_url(self, *args, **kwargs):
        # pk = get_object_or_404(kwargs['pk'])
        # post.count = F('count') + 1
        # post.save()

        pk = kwargs['pk']
        pick_member = Member.objects.filter(id=pk)
        pick_member.update(count=F('count')+1)
        return super().get_redirect_url(*args, **kwargs)


class SinglePost(TemplateView):
    template_name = "ex4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = get_object_or_404(Member,pk=self.kwargs['pk'])
        context['data'] = "THIS IS NEW"
        context['title'] = "ex4"
        return context
