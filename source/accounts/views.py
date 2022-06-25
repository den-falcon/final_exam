from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from accounts.forms import AuthUserCreationForm, AuthUserAuthenticationForm

User = get_user_model()


class LoginUser(LoginView):
    form_class = AuthUserAuthenticationForm
    template_name = 'accounts/login.html'


class RegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    form_class = AuthUserCreationForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class UserProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = "user_objects"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        if self.request.user == self.object:
            context['advertisements'] = self.object.advertisements.filter(is_deleted=False)
        else:
            context['advertisements'] = self.object.advertisements.filter(Q(status='published') & Q(is_deleted=False))
        return context
