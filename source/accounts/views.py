from django.views.generic import CreateView
from accounts.models import User
from accounts.forms import UserCreationForm


class RegisterView(CreateView):
    model = User
    template_name = 'registration/registration.html'
    form_class = UserCreationForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class UserProfileView(DetailView):
    model = Users
    template_name = 'registration/profile.html'
    context_object_name = "user_object"
