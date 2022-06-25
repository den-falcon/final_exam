from django.urls import path

from webapp.views.advertisement import AdvertisementsListView, AdvertisementsDetailView, AdvertisementsCreateView, \
    AdvertisementsUpdateView, AdvertisementsDeleteView, OnModerationAdvertisementsListView
from webapp.views.categories import CategoriesCreateView

app_name = 'webapp'

urlpatterns = [
    path('advertisements/', AdvertisementsListView.as_view(), name='advertisements_list'),
    path('advertisements/create/', AdvertisementsCreateView.as_view(), name='advertisements_create'),
    path('advertisements/<int:pk>/', AdvertisementsDetailView.as_view(), name='advertisements_detail'),
    path('advertisements/<int:pk>/update/', AdvertisementsUpdateView.as_view(), name='advertisements_update'),
    path('advertisements/<int:pk>/delete/', AdvertisementsDeleteView.as_view(), name='advertisements_delete'),
    path('advertisements/on_moderation/', OnModerationAdvertisementsListView.as_view(), name='on_moderation_list'),
    path('categories/create/', CategoriesCreateView.as_view(), name='categories_create'),
]
