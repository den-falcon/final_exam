from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AdvertisementForm
from webapp.models import Advertisement


class AdvertisementsListView(ListView):
    template_name = 'webapp/advertasement/advertisement_list.html'
    model = Advertisement
    context_object_name = 'advertisements'
    ordering = '-created_at'
    paginate_by = 10
    paginate_orphans = 0

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(status='published') & Q(is_deleted=False))
        return queryset


class OnModerationAdvertisementsListView(AdvertisementsListView):

    def get_queryset(self):
        queryset = self.model.objects.filter(Q(status='on_moderation') & Q(is_deleted=False))
        return queryset


class AdvertisementsDetailView(DetailView):
    model = Advertisement
    template_name = 'webapp/advertasement/advertisement_detail.html'
    context_object_name = 'advertisement'


class AdvertisementsCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'webapp/advertasement/advertisement_create.html'

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.author = self.request.user
        advertisement.save()
        return redirect('webapp:advertisements_list')


class AdvertisementsUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'webapp/advertasement/advertisement_update.html'

    def get_success_url(self):
        return reverse('webapp:advertisements_detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.object.author == self.request.user


class AdvertisementsDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advertisement
    template_name = "webapp/advertasement/advertisement_delete.html"
    permission_required = "webapp.delete_advertasement"

    def form_valid(self, form):
        self.object.is_delete = True
        self.object.save()
        return redirect("webapp:advertisements_list")
