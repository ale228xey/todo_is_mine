from django.contrib.auth import login
from django.views.generic import FormView
from register.forms import MyUserCreationForm


class UserRegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = MyUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
