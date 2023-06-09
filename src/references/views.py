from django.shortcuts import render
from django.views import generic
from references import models, forms
from django.urls import reverse_lazy

# Create your views here.


#CBV for Author model.

class ShowAuthors(generic.ListView):
    model = models.BookAuthor
    template_name = 'references/list_author.html'


class ShowAuthor(generic.DetailView):
    model = models.BookAuthor
    template_name = 'references/detail_author.html'


class CreateAuthor(generic.CreateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/edit_author.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateAuthor(generic.UpdateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/edit_author.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteAuthor(generic.DeleteView):
    model = models.BookAuthor
    template_name = 'references/delete_author.html'

    def get_success_url(self):
        return reverse_lazy('references:authors_list')