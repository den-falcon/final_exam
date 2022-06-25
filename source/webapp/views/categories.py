from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from webapp.forms import CategoryForm
from webapp.models import Category


class CategoriesCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'webapp/category/category_create.html'
    success_url = reverse_lazy('webapp:advertisements_list')
