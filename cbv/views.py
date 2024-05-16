from pathlib import Path

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from django.db.models import F
from django.conf import settings
from PIL import Image

from cars.models import Cars
import logging

from members.models import Member


# Create your views here.
class Ex2View(TemplateView):
    template_name = "ex2.html"

    def get_context_data(self, **kwargs):
        print("settings.MEDIA_ROOT")
        print(settings.MEDIA_ROOT)

        car = Cars.objects.get(name="57 Chevy")
        # car = Cars.objects.get(name="57 Chevy")

        print(car.photo)
        print(car.photo.name)

        path = Path(settings.MEDIA_ROOT) / car.photo.name

        print('path: ', path)

        image = Image.open(car.photo)

        print("data attr: ", image)

        context = super().get_context_data(**kwargs)

        context['data'] = "GET CONTEXT DATA"
        context['title'] = "ex2"
        context['image'] = path
        context['car'] = car

        return context


# class PostPreLoadTaskView(RedirectView):
#     pattern_name = "cbv:single-post"
#     members = Member.objects.latest("id")
#
#     def get_redirect_url(self, *args, **kwargs):
#         # pk = get_object_or_404(kwargs['pk'])
#         # post.count = F('count') + 1
#         # post.save()
#
#         pk = kwargs['pk']
#         pick_member = Member.objects.filter(id=pk)
#         pick_member.update(count=F('count') + 1)
#         return super().get_redirect_url(*args, **kwargs)


class SinglePost(TemplateView):
    template_name = "ex4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = get_object_or_404(Member, pk=self.kwargs['pk'])
        context['data'] = "THIS IS NEW"
        context['title'] = "ex4"
        return context


class Gradient(TemplateView):
    template_name = "gradient.html"
    print("GRADIENT HIT")

    pass


class FullGradient(TemplateView):
    template_name = "full_gradient.html"
    pass


class Diagonal(TemplateView):
    template_name = "diagonal.html"
    pass


class ClipPath(TemplateView):
    template_name = "clip_path.html"

    def get_context_data(self, **kwargs):
        car = Cars.objects.get(name="57 Chevy")
        context = super().get_context_data(**kwargs)
        context['car'] = car
        print('car.photo.url', car.photo.url)
        return context


class LearnSVG1(TemplateView):
    template_name = "learn_svg_1.html"

    def get_context_data(self, **kwargs):
        car = Cars.objects.get(name="57 Chevy")
        context = super().get_context_data(**kwargs)
        context['car'] = car
        print('car.photo.url', car.photo.url)
        return context


class LineDivide1(TemplateView):
    template_name = "line_divide/line_divide_1.html"
