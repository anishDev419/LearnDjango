from django.urls import path
from django.views.generic import TemplateView, RedirectView

from . import views
app_name="cbv"

urlpatterns = [
    # path('', TemplateView.as_view(template_name='ex1.html', extra_context={'title': 'Custom Title'})),
    path('', views.Ex2View.as_view(), name='ex2'),
    path('rdt', views.RedirectView.as_view(url="http://www.google.com/"), name='go-you'),
    path('ex3/<int:pk>', views.PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('ex4/<int:pk>/', views.SinglePost.as_view(), name='single-post'),
    path('gradient', views.Gradient.as_view(), name='gradient'),
    path('full-gradient', views.FullGradient.as_view(), name='full-gradient'),
    path('diagonal', views.Diagonal.as_view(), name='diagonal'),
    path('clip-path', views.ClipPath.as_view(), name='clip-path'),
    path('learn-svg', views.LearnSVG1.as_view(), name='learn-svg'),
    path('line-divide-1', views.LineDivide1.as_view(), name='line-divide-1'),


]
