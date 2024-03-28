from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from books.models import Books
from django.db.models import F
from django.utils import timezone
from .forms import AddForm


# Create your views here.
# class AddFormView(FormView):
#     template_name = "add.html"
#     form_class = AddForm
#     success_url = "/books/"
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.request.get_login_url(),
                                     self.request.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/books')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class AddFormView(CreateView):
    model = Books
    # fields = ['title']
    form_class = AddForm
    template_name = "add.html"
    success_url = "/books/"

    def get_initial(self, *args, **kwargs):
        initials = super().get_initial(**kwargs)
        # initials['title'] = 'ENTER TITLE'

        return initials


class BookEditView(UserAccessMixin, UpdateView):
    raise_exception = True
    permission_required = 'books.change_books'

    print(permission_required)

    model = Books
    template_name = "add.html"
    success_url = "/books/"
    form_class = AddForm


class IndexView(TemplateView):
    template_name = "books_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Books.objects.all()
        return context


class BookDetailView(DetailView):
    model = Books
    template_name = "book-detail.html"
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Books.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()
        return context


class BookListView(ListView):
    model = Books
    template_name = "book-list.html"
    context_object_name = "books"
    paginate_by = 1
    queryset = Books.objects.all()[:2]


class GenreView(ListView):
    model = Books
    template_name = "book-list.html"
    context_object_name = "books"
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):
        return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))
