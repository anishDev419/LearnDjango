from django.urls import path
from django.views.generic import TemplateView, RedirectView

from cbv.views import Ex2View, PostPreLoadTaskView, SinglePost, Gradient, FullGradient, Diagonal, ClipPath

app_name="cbv"

urlpatterns = [
    # path('', TemplateView.as_view(template_name='ex1.html', extra_context={'title': 'Custom Title'})),
    path('', Ex2View.as_view(), name='ex2'),
    path('rdt', RedirectView.as_view(url="http://www.google.com/"), name='go-you'),
    path('ex3/<int:pk>', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('ex4/<int:pk>/', SinglePost.as_view(), name='single-post'),
    path('gradient', Gradient.as_view(), name='gradient'),
    path('full-gradient', FullGradient.as_view(), name='full-gradient'),
    path('diagonal', Diagonal.as_view(), name='diagonal'),
    path('clip-path', ClipPath.as_view(), name='clip-path'),
]
